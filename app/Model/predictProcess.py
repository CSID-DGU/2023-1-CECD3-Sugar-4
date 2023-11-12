import subprocess
import os

# inference 실행 후 저장 코드, 추가 로직 구현 필요
# 현재 스크립트의 위치를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

def run_ser_prediction():
    kie_algorithm = "LayoutXLM"
    ser_model_dir = "inference/ser_vi_layoutxlm"
    image_dir = os.path.join(current_dir, '..', 'gui', 'down', 'kor10.jpg' )
    ser_dict_path = "utility/class_list.txt"
    vis_font_path = "PaddleOCR/doc/fonts/korean.ttf"
    ocr_order_method = "tb-yx"

    command = [
        "python",
        "PaddleOCR/ppstructure/kie/predict_kie_token_ser.py",
        f"--kie_algorithm={kie_algorithm}",
        f"--ser_model_dir={ser_model_dir}",
        f"--use_visual_backbone= {False}",
        f"--image_dir={image_dir}",
        f"--ser_dict_path={ser_dict_path}",
        f"--vis_font_path={vis_font_path}",
        f"--ocr_order_method={ocr_order_method}"
    ]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")
def run_ser_re_prediction():
    kie_algorithm = "LayoutXLM"
    re_model_dir = "inference/re_vi_layoutxlm"
    ser_model_dir = "inference/ser_vi_layoutxlm"
    image_dir = "kor43.jpg"
    ser_dict_path = "utility/class_list.txt"
    vis_font_path = "PaddleOCR/doc/fonts/korean.ttf"
    ocr_order_method = "tb-yx"

    command = [
        "python",
        "PaddleOCR/ppstructure/kie/predict_kie_token_ser_re.py",
        f"--kie_algorithm={kie_algorithm}",
        f"--re_model_dir={re_model_dir}",
        f"--ser_model_dir={ser_model_dir}",
        f"--use_visual_backbone= {False}",
        f"--image_dir={image_dir}",
        f"--ser_dict_path={ser_dict_path}",
        f"--vis_font_path={vis_font_path}",
        f"--ocr_order_method={ocr_order_method}"
    ]

    try:
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_ser_prediction()
