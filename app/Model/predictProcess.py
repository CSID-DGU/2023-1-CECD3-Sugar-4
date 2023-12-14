import subprocess
import os
import sys
from pathlib import Path

script_directory = os.path.dirname(os.path.abspath(__file__))
command_dir_ser = os.path.join(script_directory, "PaddleOCR/ppstructure/kie/predict_kie_token_ser.py")
command_dir_ser_re = os.path.join(script_directory, "PaddleOCR/ppstructure/kie/predict_kie_token_ser_re.py")
model_dir_re = os.path.join(script_directory, "inference_vi/re_vi_layoutxlm")
model_dir_ser = os.path.join(script_directory, "inference_vi/ser_vi_layoutxlm")
dict_path_ser = os.path.join(script_directory, "utility/class_list.txt")
font_path_vis = os.path.join(script_directory, "PaddleOCR/doc/fonts/korean.ttf")
requirement1_dir = os.path.join(script_directory, "PaddleOCR/requirements.txt")
requirement2_dir = os.path.join(script_directory, "PaddleOCR/ppstructure/kie/requirements.txt")

python_exe = sys.executable



def pip_upgrade():
    try:
        subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
        print("Successfully installed OpenCV.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install OpenCV: {e}")    
        
def install_requirement1():
    try:
        subprocess.check_call([python_exe, "-m", "pip", "install", "-r", requirement1_dir])
        print("Successfully installed OpenCV.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install OpenCV: {e}")
        
def install_requirement2():
    try:
        subprocess.check_call([python_exe, "-m", "pip", "install", "-r", requirement2_dir])
        print("Successfully installed OpenCV.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install OpenCV: {e}")
 
def install_nogpu():
    try:
        subprocess.check_call([python_exe, "-m", "pip", "install", "paddlepaddle", "-i",  "https://mirror.baidu.com/pypi/simple"])
        print("Successfully installed OpenCV.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install OpenCV: {e}")
       

def upgrade_paddleocr1():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "paddleocr", "-U"])
        print("PaddleOCR has been successfully upgraded.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade PaddleOCR: {e}")
        
        
def run_ser_prediction(image_dir):
    kie_algorithm = "LayoutXLM"
    ser_model_dir = model_dir_ser
    ser_dict_path = dict_path_ser
    vis_font_path = font_path_vis
    ocr_order_method = "tb-yx"  

    command = [
        python_exe,
        command_dir_ser,
        f"--kie_algorithm={kie_algorithm}",
        f"--ser_model_dir={ser_model_dir}",
        f"--use_visual_backbone={False}",
        f"--image_dir={image_dir}",
        f"--ser_dict_path={ser_dict_path}",
        f"--vis_font_path={vis_font_path}",
        f"--ocr_order_method={ocr_order_method}"
    ]
    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  stdin=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            print(f"Error: {stderr.decode()}")
        else:
            print(stdout.decode())
    except Exception as e:
        print(f"An error occurred: {e}")

def run_ser_re_prediction(image_dir):
    kie_algorithm = "LayoutXLM"
    re_model_dir = model_dir_re
    ser_model_dir = model_dir_ser
    ser_dict_path = dict_path_ser
    vis_font_path = font_path_vis
    ocr_order_method = "tb-yx"

    command = [
        python_exe,
        command_dir_ser_re,
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
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,  stdin=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            print(f"Error: {stderr.decode()}")
        else:
            print(stdout.decode())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python predictProcess.py <function_name> <image_dir>")
        sys.exit(1)
        
        
    pip_upgrade()
    install_requirement1()
    install_requirement2()
    install_nogpu()
    upgrade_paddleocr1()

    function_name = sys.argv[1]
    image_dir = sys.argv[2]
    
    if function_name == "ser":
        run_ser_prediction(image_dir)
    elif function_name == "ser_re":
        run_ser_re_prediction(image_dir)
    else:
        print("Invalid function name. Choose either 'ser' or 'ser_re'.")
