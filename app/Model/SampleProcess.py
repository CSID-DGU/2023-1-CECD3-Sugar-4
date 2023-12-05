import os
from paddleocr import PaddleOCR
import json
import sys
import ast

def load_privacy_boxes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        return ast.literal_eval(data)

def run_ocr(img_path):
    ocr = PaddleOCR(lang="korean")
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
            
        
if __name__ == "__main__":
    # 현재 디렉토리 설정
    base_dir = os.getcwd()
    results_dir = os.path.join(base_dir, 'app', 'gui', 'Results')
    
    current_dir = sys.argv[1]
    selected_file_dir = sys.argv[2]
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
    save_results_to_text_file(formatted_matches, result_file_dir, file_name_without_extension)