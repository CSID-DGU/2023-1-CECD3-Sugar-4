# 2023-1-CDCD3-Sugar-4
 
2023년도 컴퓨터공학종합설계 Sugar조

## <h1> 팀원</h1>
|이름|학과|학번|역할|
|---|---|---|---|
|고대호|수학과|2018110417|팀장,OCR 데이터 전처리 및 학습, 개인정보 식별 기능 구현 |
|김민철|수학과|2018110424|GUI 개발, 데이터 라벨링|
|김용권|수학과|2018110407|모델 학습, 데이터 라벨링, 애플리케이션 기능 구현|
|변찬현|수학과|2018110399|GUI 개발, 데이터 라벨링|


## <h1> 소개 </h1>
이력서, 지원서 등과 같이 양식이 있는 문서 이미지에서 개인정보를 자동으로 찾고 비식별화 해주는 프로세스 입니다.

## <h1> 사용 방법</h1>

Python 3.10.11 에서 작업하였습니다.
```bash
git clone https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4.git
cd 2023-1-CECD3-Sugar-4
pip install -r requirements.txt
pip install paddlepaddle 
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddleocr -U
cd app && cd model && cd utility
python download_model.py
cd ../.. && cd ../.. && cd ../..
python sugar.py
```

## <h1>  실행 화면 </h1>

