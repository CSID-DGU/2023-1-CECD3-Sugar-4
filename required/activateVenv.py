import os
import tarfile
import platform
import subprocess

def unpack_and_activate_environment(env_archive_path, env_directory):
    try:
        # Create the target directory if it doesn't exist
        os.makedirs(env_directory, exist_ok=True)

        # Unpack the environment from the archive
        with tarfile.open(env_archive_path, "r:gz") as tar:
            tar.extractall(path=env_directory)
            print(f"Unpacked the environment into {env_directory}")

        # Activate the environment
        if platform.system() == 'Windows':
            activate_script = os.path.join(env_directory, "Scripts", "activate.bat")
            subprocess.run(activate_script, shell=True)
        else:
            activate_script = os.path.join(env_directory, "bin", "activate")
            subprocess.run(f"source {activate_script}", shell=True)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    env_archive_path = "project_env.tar.gz"  # 배포된 환경 압축 파일 경로
    env_directory = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "venv")  # 한 단계 상위 디렉토리에 환경 디렉토리 생성

    # Unpack and activate the environment
    unpack_and_activate_environment(env_archive_path, env_directory)

"""
가상환경 실행 코드 수정 필요
"""