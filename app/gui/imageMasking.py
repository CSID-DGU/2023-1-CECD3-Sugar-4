import json
import cv2
import os

def mask_image_with_bboxes(json_file_path, image_file_path, output_path):
    # JSON 파일에서 바운딩 박스 데이터를 읽어옵니다.
    with open(json_file_path, 'r', encoding='utf-8') as file:
        bboxes = json.load(file)

    # 이미지를 불러옵니다.
    image = cv2.imread(image_file_path)

    # 각 바운딩 박스에 대해 마스킹을 수행합니다.
    for bbox_dict in bboxes:
        bbox = bbox_dict['bbox']
        x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), -1)  # 검은색으로 마스킹

    # 결과 이미지를 저장합니다.
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    parts = json_file_path.split(os.sep)    
    base_sample_name = parts[-2] 
    base_name = os.path.basename(image_file_path)
    file_name, file_ext = os.path.splitext(base_name)
    masked_file_name = f"masked_{file_name}{file_ext}"
    output_file_path = os.path.join(output_path, base_sample_name, masked_file_name)
    cv2.imwrite(output_file_path, image)