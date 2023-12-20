# 2023-1-CECD3-Sugar-4
 
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
pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
pip install paddleocr -U
cd app && cd Model && cd utility
python download_model.py
cd .. && cd .. && cd ..
python sugar.py
```

## <h1>  실행 화면 </h1>

## 1. 시작 화면

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/5aa3593b-0182-4b31-80fd-a807db071769"  width="500" height="300"/>

#### 애플리케이션 실행시 나타나는 화면 상태 입니다. 
#### 개인정보의 비식별화 프로세스를 진행하기 위한 탭들과 사용자 매뉴얼이 존재합니다.


## 2. 개인정보 자동 인식

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/0978b62e-e886-4c0a-8459-ad79f2a24a1e"  width="500" height="300"/>

#### 처리할 파일의 업로드와 삭제가 가능한 화면입니다.
#### 체크박스와 개인정보 자동 인식 버튼을 통해 단일 문서에 대한 개인정보 식별 로직을 적용할 수 있습니다.

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/cfcaba2f-9844-408e-956c-dd2f78070ff4"  width="500" height="300"/>

#### 개인정보 식별 로직 실행 결과 화면입니다.
#### 식별한 영역을 삭제하거나 추가, 수정할 수 있으며 Save 버튼을 통해 샘플로 등록이 가능합니다.
#### Masking 버튼을 눌러 입력한 문서의 개인정보를 비식별 처리한 결과물로 생성이 가능합니다.

## 3. 샘플 문서

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/9747aaf4-531a-4fd0-9a38-080152090e8a"  width="500" height="300"/>

#### 등록한 샘플 문서 이미지의 미리보기 및 개인정보 바운딩 박스 수정이 가능합니다.
#### 동일한 양식의 문서에서 비식별화할 항목을 사용자의 의도에 맞게 수정이 가능합니다.

## 4. 샘플 문서 내부

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/75817d06-a43a-4d86-a6cd-baa720511be2"  width="500" height="300"/>

#### 샘플 문서 목록의 폴더를 더블 클릭하여 내부로 이동할 수 있습니다.
#### 샘플 문서와 동일한 양식의 문서를 업로드하여 여러 개의 문서를 동시에 비식별화 처리가 가능합니다.

## 5. 결과 화면 및 수정

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/57dedb41-2b26-46f5-8af8-68f1e1afef42"  width="500" height="300"/>


<div style="text-align: center; margin-left: -120px; font-size: 50px;">⬇️</div>

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/abba0b27-d8d6-42cd-9028-86c142702f4d"  width="500" height="300"/>

#### 사용자가 GUI를 통해 최종적으로 개인정보를 수정 및 저장할 수 있습니다.


## 6. 결과 다운로드

<img src="https://github.com/CSID-DGU/2023-1-CECD3-Sugar-4/assets/113659537/8468e7c9-9922-4227-a020-4a3b359429a3"  width="500" height="300"/>

#### 단일 문서를 처리한 경우 {masked_이미지명.jpg} 파일로 생성됩니다.
#### 샘플 문서를 통해 처리한 경우 샘플 폴더 내부에 {masked_이미지명.jpg} 파일로 생성됩니다.
#### 파일 또는 폴더 전체를 다운로드 할 수 있습니다.

