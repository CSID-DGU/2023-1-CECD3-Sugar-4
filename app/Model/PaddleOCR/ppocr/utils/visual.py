# copyright (c) 2021 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import cv2
import os
import numpy as np
import re
from PIL import Image, ImageDraw, ImageFont



def draw_ser_results(image,
                     ocr_results,
                     font_path="doc/fonts/simfang.ttf",
                     font_size=14):
    np.random.seed(2021)
    color = (np.random.permutation(range(255)),
             np.random.permutation(range(255)),
             np.random.permutation(range(255)))
    color_map = {
        idx: (color[0][idx], color[1][idx], color[2][idx])
        for idx in range(1, 255)
    }
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    elif isinstance(image, str) and os.path.isfile(image):
        image = Image.open(image).convert('RGB')
    img_new = image.copy()
    draw = ImageDraw.Draw(img_new)

    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    for ocr_info in ocr_results:
        if ocr_info["pred_id"] not in color_map:
            continue
        color = color_map[ocr_info["pred_id"]]
        text = "{}: {}".format(ocr_info["pred"], ocr_info["transcription"])

        if "bbox" in ocr_info:
            # draw with ocr engine
            bbox = ocr_info["bbox"]
        else:
            # draw with ocr groundtruth
            bbox = trans_poly_to_bbox(ocr_info["points"])
        draw_box_txt(bbox, text, draw, font, font_size, color)

    img_new = Image.blend(image, img_new, 0.7)
    return np.array(img_new)


def draw_box_txt(bbox, text, draw, font, font_size, color):

    # draw ocr results outline
    bbox = ((bbox[0], bbox[1]), (bbox[2], bbox[3]))
    draw.rectangle(bbox, fill=color)

    # draw ocr results
    left, top, right, bottom = font.getbbox(text)
    tw, th = right - left, bottom - top
    start_y = max(0, bbox[0][1] - th)
    draw.rectangle(
        [(bbox[0][0] + 1, start_y), (bbox[0][0] + tw + 1, start_y + th)],
        fill=(0, 0, 255))
    draw.text((bbox[0][0] + 1, start_y), text, fill=(255, 255, 255), font=font)


def trans_poly_to_bbox(poly):
    x1 = np.min([p[0] for p in poly])
    x2 = np.max([p[0] for p in poly])
    y1 = np.min([p[1] for p in poly])
    y2 = np.max([p[1] for p in poly])
    return [x1, y1, x2, y2]


def draw_re_results(image,
                    result,
                    font_path="doc/fonts/simfang.ttf",
                    font_size=18):
    np.random.seed(0)
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    elif isinstance(image, str) and os.path.isfile(image):
        image = Image.open(image).convert('RGB')
    img_new = image.copy()
    draw = ImageDraw.Draw(img_new)

    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    color_head = (0, 0, 255)
    color_tail = (255, 0, 0)
    color_line = (0, 255, 0)

    for ocr_info_head, ocr_info_tail in result:
        privacy = ['성명', '주소', '휴대전화','이메일','연락처','생년월일', '이름']
        if ocr_info_head["transcription"] in privacy :
            draw_box_txt(ocr_info_head["bbox"], ocr_info_head["transcription"],
                     draw, font, font_size, color_head)
            draw_box_txt(ocr_info_tail["bbox"], ocr_info_tail["transcription"],
                     draw, font, font_size, color_tail)

            center_head = (
                (ocr_info_head['bbox'][0] + ocr_info_head['bbox'][2]) // 2,
                (ocr_info_head['bbox'][1] + ocr_info_head['bbox'][3]) // 2)
            center_tail = (
                (ocr_info_tail['bbox'][0] + ocr_info_tail['bbox'][2]) // 2,
                (ocr_info_tail['bbox'][1] + ocr_info_tail['bbox'][3]) // 2)
        else :
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            email_match = re.match(email_pattern, ocr_info_tail["transcription"])
            if email_match:
                draw_box_txt(ocr_info_tail["bbox"], ocr_info_tail["transcription"],
                             draw, font, font_size, color_line)
            phone_pattern = r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b'
            phone_match = re.match(phone_pattern, ocr_info_tail["transcription"])
            if phone_match:
                draw_box_txt(ocr_info_tail["bbox"], ocr_info_tail["transcription"],
                             draw, font, font_size, color_line)

    img_new = Image.blend(image, img_new, 0.5)
    return np.array(img_new)


def draw_rectangle(img_path, boxes):
    boxes = np.array(boxes)
    img = cv2.imread(img_path)
    img_show = img.copy()
    for box in boxes.astype(int):
        x1, y1, x2, y2 = box
        cv2.rectangle(img_show, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return img_show


def calculate_minimum_bounding_box(bboxes):
    min_x = min(bbox[0] for bbox in bboxes)
    min_y = min(bbox[1] for bbox in bboxes)
    max_x = max(bbox[2] for bbox in bboxes)
    max_y = max(bbox[3] for bbox in bboxes)
    return [min_x, min_y, max_x, max_y]

def extract_privacy_bboxes(result):
    bbox_groups = {}
    privacy_keywords = ['성명', '주소', '휴대전화', '이메일', '연락처', '생년월일', '이름',
                        '교수','주민등록번호', '여권번호', '외국인등록번호', '운전면허번호',
                        '면허증', '성함',' 사는곳', '거주지', '생일', '취득일', '휴대폰',
                        '전화번호', '팩스', '핸드폰', '전화', '의료기록번호', '건강보험번호',
                        '번호', '계좌', '계좌번호', '통장', '카드번호', '신용카드', '차량번호',
                        '일련번호', 'IP', 'IP주소', '식별코드', '아이디', '비밀번호', '군번',
                        '등록번호', '성별', '연령', '나이', '국적', '고향', '우편', '병명',
                        '등급', '학교', '학과', '전공', '학력', '직업', '직장', '직장명',
                        '부서', '직급', '계급', '배우자', '자녀', '부모', '형제', '법정대리인',
                        '학번', '계정', '진료번호','관계','서명','본적' ]
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_pattern = r'\b\d{3}[-.\s]?\d{3,4}[-.\s]?\d{4}\b'
    credit_card_pattern = r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'

    for ocr_info_head, ocr_info_tails in result:
        key_head = ocr_info_head["transcription"]

        # Ensure ocr_info_tails is a list
        if not isinstance(ocr_info_tails, list):
            ocr_info_tails = [ocr_info_tails]

        # If there are multiple tails per head, iterate over all tails
        for ocr_tail_info in ocr_info_tails:
            key_tail = ocr_tail_info["transcription"]

            # Check if any privacy-related keyword is present in the head
            if any(keyword in key_head for keyword in privacy_keywords):
                bbox_groups.setdefault(key_head, []).append(ocr_tail_info["bbox"])
            else:
                if re.match(email_pattern, key_tail) or re.match(phone_pattern, key_tail or re.match(credit_card_pattern, key_tail)):
                    bbox_groups.setdefault(key_head, []).append(ocr_tail_info["bbox"])

    merged_bboxes = []
    for privacy_key, bboxes in bbox_groups.items():
        if privacy_key == '주소':
            merged_bbox = calculate_minimum_bounding_box(bboxes)
            merged_bboxes.append(merged_bbox)
        else:
            merged_bboxes.extend(bboxes)

    return merged_bboxes