import subprocess
import sys

def create_conda_env():
    try:
        # Conda 환경 생성
        subprocess.check_call([sys.executable, '-m', 'conda', 'env', 'create', '-f', 'requirements.yml'])
    except subprocess.CalledProcessError as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    create_conda_env()

"""수정 필요"""