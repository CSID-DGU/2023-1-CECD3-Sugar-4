import subprocess
import os
import sys

def run_ser_prediction(image_dir):
    kie_algorithm = "LayoutXLM"
    ser_model_dir = "app/Model/inference/ser_vi_layoutxlm"
    ser_dict_path = "app/Model/utility/class_list.txt"
    vis_font_path = "app/Model/PaddleOCR/doc/fonts/korean.ttf"
    ocr_order_method = "tb-yx"

    command = [
        "python",
        "app/Model/PaddleOCR/ppstructure/kie/predict_kie_token_ser.py",
        f"--kie_algorithm={kie_algorithm}",
        f"--ser_model_dir={ser_model_dir}",
        f"--use_visual_backbone={False}",
        f"--image_dir={image_dir}",
        f"--ser_dict_path={ser_dict_path}",
        f"--vis_font_path={vis_font_path}",
        f"--ocr_order_method={ocr_order_method}"
    ]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_ser_re_prediction(image_dir):
    kie_algorithm = "LayoutXLM"
    re_model_dir = "app/Model/inference/re_vi_layoutxlm"
    ser_model_dir = "app/Model/inference/ser_vi_layoutxlm"
    ser_dict_path = "app/Model/utility/class_list.txt"
    vis_font_path = "app/Model/PaddleOCR/doc/fonts/korean.ttf"
    ocr_order_method = "tb-yx"

    command = [
        "python",
        "app/Model/PaddleOCR/ppstructure/kie/predict_kie_token_ser_re.py",
        f"--kie_algorithm={kie_algorithm}",
        f"--re_model_dir={re_model_dir}",
        f"--ser_model_dir={ser_model_dir}",
        f"--use_visual_backbone={False}",
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
    if __name__ == "__main__":
        # 명령행 인수로 파일 경로 받아오기
        if len(sys.argv) != 3:
            print("Usage: python predictProcess.py <function_name> <image_dir>")
            sys.exit(1)

        function_name = sys.argv[1]
        image_dir = sys.argv[2]

        if function_name == "ser":
            run_ser_prediction(image_dir)
        elif function_name == "ser_re":
            run_ser_re_prediction(image_dir)
        else:
            print("Invalid function name. Choose either 'ser' or 'ser_re'.")
