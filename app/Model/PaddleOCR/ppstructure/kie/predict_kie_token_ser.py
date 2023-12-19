# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '../..')))

os.environ["FLAGS_allocator_strategy"] = 'auto_growth'

import ast
import cv2
import json
import numpy as np
import time
from pathlib import Path

import tools.infer.utility as utility
from ppocr.data import create_operators, transform
from ppocr.postprocess import build_post_process
from ppocr.utils.logging import get_logger
from ppocr.utils.visual import draw_ser_results
from ppocr.utils.utility import get_image_file_list, check_and_read
from ppstructure.utility import parse_args

from paddleocr import PaddleOCR

logger = get_logger()


class SerPredictor(object):
    def __init__(self, args):
        self.ocr_engine = PaddleOCR(
            use_angle_cls=args.use_angle_cls,
            det_model_dir=args.det_model_dir,
            rec_model_dir=args.rec_model_dir,
            show_log=False,
            use_gpu=args.use_gpu)

        pre_process_list = [{
            'VQATokenLabelEncode': {
                'algorithm': args.kie_algorithm,
                'class_path': args.ser_dict_path,
                'contains_re': False,
                'ocr_engine': self.ocr_engine,
                'order_method': args.ocr_order_method,
            }
        }, {
            'VQATokenPad': {
                'max_seq_len': 512,
                'return_attention_mask': True
            }
        }, {
            'VQASerTokenChunk': {
                'max_seq_len': 512,
                'return_attention_mask': True
            }
        }, {
            'Resize': {
                'size': [224, 224]
            }
        }, {
            'NormalizeImage': {
                'std': [58.395, 57.12, 57.375],
                'mean': [123.675, 116.28, 103.53],
                'scale': '1',
                'order': 'hwc'
            }
        }, {
            'ToCHWImage': None
        }, {
            'KeepKeys': {
                'keep_keys': [
                    'input_ids', 'bbox', 'attention_mask', 'token_type_ids',
                    'image', 'labels', 'segment_offset_id', 'ocr_info',
                    'entities'
                ]
            }
        }]
        postprocess_params = {
            'name': 'VQASerTokenLayoutLMPostProcess',
            "class_path": args.ser_dict_path,
        }

        self.preprocess_op = create_operators(pre_process_list,
                                              {'infer_mode': True})
        self.postprocess_op = build_post_process(postprocess_params)
        self.predictor, self.input_tensor, self.output_tensors, self.config = \
            utility.create_predictor(args, 'ser', logger)

    def __call__(self, img):
        ori_im = img.copy()
        data = {'image': img}
        data = transform(data, self.preprocess_op)
        if data[0] is None:
            return None, 0
        starttime = time.time()

        for idx in range(len(data)):
            if isinstance(data[idx], np.ndarray):
                data[idx] = np.expand_dims(data[idx], axis=0)
            else:
                data[idx] = [data[idx]]

        for idx in range(len(self.input_tensor)):
            self.input_tensor[idx].copy_from_cpu(data[idx])

        self.predictor.run()

        outputs = []
        for output_tensor in self.output_tensors:
            output = output_tensor.copy_to_cpu()
            outputs.append(output)
        preds = outputs[0]

        post_result = self.postprocess_op(
            preds, segment_offset_ids=data[6], ocr_infos=data[7])
        elapse = time.time() - starttime
        return post_result, data, elapse


def main(args):
    image_file_list = get_image_file_list(args.image_dir)
    ser_predictor = SerPredictor(args)
    count = 0
    total_time = 0

    os.makedirs(args.output, exist_ok=True)
    with open(
            os.path.join(args.output, 'infer.txt'), mode='a',
            encoding='utf-8') as f_w:
        for image_file in image_file_list:
            img, flag, _ = check_and_read(image_file)
            if not flag:
                img = cv2.imread(image_file)
                img = img[:, :, ::-1]
            if img is None:
                logger.info("error in loading image:{}".format(image_file))
                continue
            ser_res, _, elapse = ser_predictor(img)
            ser_res = ser_res[0]
            res_str = '{}\t{}\n'.format(
                image_file,
                json.dumps(
                    {
                        "ocr_info": ser_res,
                    }, ensure_ascii=False))
            f_w.write(res_str)
            img_res = draw_ser_results(
                image_file,
                ser_res,
                font_path=args.vis_font_path, )
            img_save_path = os.path.join(args.output,
                                         os.path.basename(image_file))
            cv2.imwrite(img_save_path, img_res)
            logger.info("save vis result to {}".format(img_save_path))
            if count > 0:
                total_time += elapse
            count += 1
            logger.info("Predict time of {}: {}".format(image_file, elapse))

script_directory = Path(__file__).resolve().parent
base_dir = script_directory.parents[4]
def load_privacy_boxes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        return ast.literal_eval(data)

def run_ocr(img_path):
    ocr = PaddleOCR(det_model_dir = os.path.join(script_directory.parents[3], 'Model', 'inference_OCR','kor_PP-OCRv3_det'), rec_model_dir = os.path.join(script_directory.parents[3], 'Model', 'inference_OCR','kor_PP-OCRv3_rec'), rec = False)
    result = ocr.ocr(img_path, cls=False)

    ocr_result = []
    for i in range(len(result[0])):
        ocr_item = result[0][i][0]
        ocr_result.append(ocr_item)
    
    return ocr_result

def convert_ocr_result_to_bbox_corrected(ocr_data):
    """ Convert OCR data in polygon format to bbox format (x, y, width, height) correctly. """
    bboxes = []
    for polygon in ocr_data:
        x_coords = [point[0] for point in polygon]
        y_coords = [point[1] for point in polygon]
        x_min = min(x_coords)
        y_min = min(y_coords)
        x_max = max(x_coords)
        y_max = max(y_coords)
        bbox = [x_min, y_min, x_max - x_min, y_max - y_min]
        bboxes.append(bbox)
    return bboxes


def calculate_iou(bbox1, bbox2):
    """ Calculate the Intersection over Union (IoU) of two bounding boxes. """
    x_left = max(bbox1[0], bbox2[0])
    y_top = max(bbox1[1], bbox2[1])
    x_right = min(bbox1[0] + bbox1[2], bbox2[0] + bbox2[2])
    y_bottom = min(bbox1[1] + bbox1[3], bbox2[1] + bbox2[3])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    bbox1_area = bbox1[2] * bbox1[3]
    bbox2_area = bbox2[2] * bbox2[3]
    iou = intersection_area / float(bbox1_area + bbox2_area - intersection_area)
    return iou

def find_matching_bboxes(known_bboxes, new_bboxes, iou_threshold):
    """ Find matching bounding boxes based on IoU threshold. """
    matches = []
    for new_bbox in new_bboxes:
        for known_bbox in known_bboxes:
            iou = calculate_iou(new_bbox, known_bbox)
            if iou >= iou_threshold:
                matches.append((new_bbox, known_bbox, iou))
    return matches

def find_matches_and_format_output(priv_boxes, ocr_boxes, threshold=0.01):
    formatted_matches = []
    for priv in priv_boxes:
        for ocr in ocr_boxes:
            iou = calculate_iou(priv, ocr)
            if iou >= threshold:
                bbox_x2 = ocr[0] + ocr[2]
                bbox_y2 = ocr[1] + ocr[3]
                formatted_matches.append({'bbox': [ocr[0], ocr[1], bbox_x2, bbox_y2]})
                break 
    return formatted_matches

def save_results_to_text_file(results, output_dir, file_name):
    output_file_path = os.path.join(output_dir, file_name + '.txt')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        results_str = json.dumps(results, indent=4)
        f.write(results_str)
    return output_dir
            
        
def predict_by_sample(current_dir, selected_file_dir) :
    # 현재 디렉토리 설정
    results_dir = os.path.join(base_dir, 'app', 'gui', 'Results')
    file_name_without_extension = os.path.splitext(os.path.basename(selected_file_dir))[0]

    image_dir = os.path.join(current_dir, '..')
    corrected_dir = os.path.abspath(image_dir)
    bbox_file_name = os.path.basename(corrected_dir) + "_privacy_bbox.txt"
    bbox_file_path = os.path.join(image_dir, bbox_file_name)

    # 개인 정보 보호 박스 파일 로드
    sample_privacy = load_privacy_boxes(bbox_file_path)

    # OCR 실행
    ocr_result = run_ocr(selected_file_dir)
    
    converted_sample_privacy = []
    for entry in sample_privacy:
        bbox = entry['bbox']
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        converted_sample_privacy.append([bbox[0], bbox[1], width, height])

    converted_ocr_result_corrected = convert_ocr_result_to_bbox_corrected(ocr_result)

    formatted_matches = find_matches_and_format_output(converted_sample_privacy, converted_ocr_result_corrected)
    
    result_file_dir = os.path.join(results_dir, os.path.basename(corrected_dir))
    if not os.path.exists(result_file_dir):
        os.makedirs(result_file_dir)

    # 결과 저장
    output_dir = save_results_to_text_file(formatted_matches, result_file_dir, file_name_without_extension)
    return output_dir

if __name__ == "__main__":
    main(parse_args())
