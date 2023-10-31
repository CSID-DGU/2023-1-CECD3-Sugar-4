import os
import subprocess

# run only one time
# Clone the PaddleOCR repository
git_repo_url = "https://github.com/PaddlePaddle/PaddleOCR.git"
destination_dir = "C:\\Users\\gwonl\\Desktop\\2023-1-CECD3-Sugar-4\\app\\Model\\PaddleOCR"  # 경로 지정 따로 처리 필요

# Clone the repository to the specified directory
subprocess.run(["git", "clone", git_repo_url, destination_dir])

# Change the current working directory to the cloned PaddleOCR directory
os.chdir(destination_dir)

# Install required packages from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])
subprocess.run(["pip", "install", "-r", "ppstructure/kie/requirements.txt"])

# Upgrade the PaddleOCR package
subprocess.run(["pip", "install", "paddleocr", "-U"])

# Install PaddlePaddle with a specified mirror
subprocess.run(["python", "-m", "pip", "install", "paddlepaddle", "-i", "https://mirror.baidu.com/pypi/simple"])

# If you have GPU device, run following code
"""
subprocess.run(["python", "-m", "pip", "install", "paddlepaddle-gpu", "-i", "https://mirror.baidu.com/pypi/simple"])
"""

# Install PaddleOCR (version 2.6.0.3 or higher)
paddleocr_version = ">=2.6.0.3"
subprocess.run(["pip3", "install", f"paddleocr{paddleocr_version}"])

# Install the image direction classification dependency package PaddleClas (if needed)
paddleclas_version = ">=2.4.3"
subprocess.run(["pip3", "install", f"paddleclas{paddleclas_version}"])

# Install PaddleNLP (version 2.5.2)
subprocess.run(["pip", "install", "paddlenlp==2.5.2"])

# font
subprocess.run(["pip", "install", "--upgrade", "pillow"])