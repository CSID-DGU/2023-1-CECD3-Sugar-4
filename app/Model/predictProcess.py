import subprocess

# inference 실행 후 저장 코드
def run_ser_prediction():
    kie_algorithm = "LayoutXLM"
    ser_model_dir = "inference/ser_vi_layoutxlm"
    use_visual_backbone = False
    image_dir = "image_name.jpg"
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
    use_visual_backbone = False
    image_dir = "image_name.jpg"
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
