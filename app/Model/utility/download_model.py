import gdown
import os
import zipfile

# 파일 ID와 다운로드 경로를 설정
file_link = "https://drive.google.com/file/d/1WpkqQo1oFMMBrWqFavRbii1-RaFFAzFj/view?usp=drive_link"
file_id = file_link.split("/d/")[1].split("/view")[0]

# 상위 폴더로 이동
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# 다운로드한 파일을 저장할 경로
output_path = os.path.join(parent_directory, 'inference.zip')
"""
# 파일 다운로드
gdown.download(f'https://drive.google.com/uc?id={file_id}', output_path, quiet=False)
"""
# 압축을 해제할 경로
new_directory_name = 'inference'  # 새로운 디렉토리 이름
extraction_directory = os.path.join(parent_directory, new_directory_name)

with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_directory)

# 다운로드한 zip 파일 삭제
os.remove(output_path)
