import subprocess
import sys
from pathlib import Path

from userProcess import LabelingTool

current_path = Path(__file__).resolve().parent
sys.path.append(str(current_path / 'UI'))

from enum import Enum
import os
import shutil
import subprocess
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QWidget, QListWidget
from PySide6.QtCore import QDir, Qt, Slot, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from ui_2 import Ui_MainWindow2
from ui_3 import Ui_MainWindow3
from ui_4 import Ui_MainWindow4
from ui_6 import Ui_MainWindow6
from ui_8 import Ui_MainWindow8

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

class CheckableItem(QStandardItem):
    def __init__(self, text, is_folder=False):
        super(CheckableItem, self).__init__(text)
        self.is_folder = is_folder
        self.setCheckable(True)
        self.setCheckState(Qt.Unchecked)

class UI_2App(QMainWindow):
    def __init__(self):
        super(UI_2App, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.close_ui_2_and_open_ui_4)
        # pushButton_3클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_4.clicked.connect(self.close_ui_2_and_open_ui_3)
        self.ui.pushButton_6.clicked.connect(self.close_ui_2_and_open_ui_6)

    @Slot()
    def close_ui_2_and_open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()

    @Slot()
    def close_ui_2_and_open_ui_3(self):
        # pushButton_4를 클릭했을 때 실행될 함수입니다.
        # UI_3App 인스턴스를 생성하여 UI_3 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
        
    @Slot()
    def close_ui_2_and_open_ui_6(self):
        # pushButton_4를 클릭했을 때 실행될 함수입니다.
        # UI_3App 인스턴스를 생성하여 UI_3 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

class UI_3App(QMainWindow):
    def __init__(self):
        super(UI_3App, self).__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.close_ui_3_and_open_ui_4)
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_3_and_open_ui_2)
        self.ui.pushButton_6.clicked.connect(self.close_ui_3_and_open_ui_6)
        self.ui.pushButton_4.clicked.connect(self.run_predict_process)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
# Set the directory to a relative path within the script's directory
        directory = os.path.join(script_directory, 'down')

        self.show_file_list(directory)

    def show_file_list(self, directory):
        file_list = os.listdir(directory)
        filtered_files = file_list

        model = QStandardItemModel()
        for item_text in filtered_files:
            item = CheckableItem(item_text)
            model.appendRow(item)

        # 모델에 itemChanged 시그널 연결
        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.pushButton_9.clicked.connect(self.upload_file)
        self.model=model
        
    def upload_file(self):
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(self, "파일 선택", "", "모든 파일 (*);;텍스트 파일 (*.txt);;이미지 파일 (*.png *.jpg)")

        destination_directory = os.path.join(self.current_dir, 'down')

        for file_path in file_paths:
            # 목적지 디렉토리를 명시적인 경로로 수정
            destination_path = os.path.join(destination_directory, os.path.basename(file_path))

            try:
                # 파일을 목적지 경로로 복사
                shutil.copy(file_path, destination_path)
                item = CheckableItem(os.path.basename(destination_path))
                self.model.appendRow(item)
            except Exception as e:
                print(f"파일 업로드 중 오류 발생: {str(e)}")
        
    # itemChanged 시그널을 처리하는 슬롯
    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        if item.checkState() == Qt.Checked:
            # 아이템이 체크될 때 다른 모든 아이템의 체크를 해제
            model = item.model()
            for row in range(model.rowCount()):
                if model.item(row) != item:
                    model.item(row).setCheckState(Qt.Unchecked)

    def get_selected_file_name(self):
        model = self.ui.listView.model()
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        if selected_items:
            file_name = selected_items[0].text()
            directory = os.path.join('app','gui', 'down')  # 또는 원하는 디렉토리로 수정
            file_path = os.path.join(directory, file_name)
            return file_path
        else:
            return None

    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            # 선택한 항목의 파일 경로
            file_path = os.path.join(directory, item.text())

            try:
                os.remove(file_path)  # 파일 삭제
                model.removeRow(item.row())  # 모델에서 항목 제거
            except OSError as e:
                print(f"Failed to delete {item.text()}: {str(e)}")

    @Slot()
    def run_predict_process(self):
        selected_file_name = self.get_selected_file_name()

        if selected_file_name:
            other_directory = os.path.join(self.current_dir, '..', 'Model')
            predict_process_path = os.path.join(other_directory, 'predictProcess.py')
            function_name = 'ser_re'  # 'ser' 또는 'ser_re' 중 선택

            try:
                base_name = os.path.basename(selected_file_name)
                file_name, _ = os.path.splitext(base_name)

                # SampleRepo, Results, SampleRepo/이미지파일명, Results/이미지파일명 폴더 생성
                for dir_name in ['SampleRepo', 'Results']:
                    dir_path = os.path.join('app', 'gui', dir_name)
                    specific_dir_path = os.path.join(dir_path, file_name)

                    for path in [dir_path, specific_dir_path]:
                        if not os.path.exists(path):
                            os.makedirs(path)

                # 입력받은 파일을 SampleRepo/이미지파일명 내부에 복사
                sample_repo_dir = os.path.join('app', 'gui', 'SampleRepo', file_name)
                shutil.copy2(selected_file_name, sample_repo_dir)

                subprocess.run(["python", predict_process_path, function_name, selected_file_name])

            except Exception as e:
                print(f"An error occurred: {e}")

    @Slot()
    def close_ui_3_and_open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()

    @Slot()
    def close_ui_3_and_open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
    
    @Slot()
    def close_ui_3_and_open_ui_6(self):
        # pushButton_6를 클릭했을 때 실행될 함수입니다.
        # UI_6App 인스턴스를 생성하여 UI_6 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

class UI_4App(QMainWindow):
    def __init__(self):
        super(UI_4App, self).__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_4_and_open_ui_2)
        # pushButton_6 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_6.clicked.connect(self.close_ui_4_and_open_ui_6)
        self.ui.pushButton_8.clicked.connect(self.close_ui_4_and_open_ui_3)
        
    @Slot()
    def close_ui_4_and_open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
        
    @Slot()
    def close_ui_4_and_open_ui_6(self):
        # pushButton_6를 클릭했을 때 실행될 함수입니다.
        # UI_6App 인스턴스를 생성하여 UI_6 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

    @Slot()
    def close_ui_4_and_open_ui_3(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()

class UI_6App(QMainWindow):
    def __init__(self):
        super(UI_6App, self).__init__()
        self.ui = Ui_MainWindow6()  # UI_6App의 UI 사용
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.close_ui_6_and_open_ui_2)
        self.ui.pushButton_2.clicked.connect(self.close_ui_6_and_open_ui_4)
        self.ui.pushButton_8.clicked.connect(self.close_ui_6_and_open_ui_3)
        self.ui.pushButton_4.clicked.connect(self.run_labeling_tool)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(self.current_dir, 'SampleRepo')
        self.show_file_list(directory)

        self.selected_file_path = ""
        
    def show_file_list(self, directory):
        file_list = os.listdir(directory)
        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)
            
        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.listView.clicked.connect(self.display_image_preview)
        self.ui.listView.doubleClicked.connect(lambda index: self.show_folder_contents(model, directory, index))

    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        # UI_6App의 기능을 그대로 유지합니다.
        if item.checkState() == Qt.Checked:
            model = item.model()
            for row in range(model.rowCount()):
                if model.item(row) != item:
                    model.item(row).setCheckState(Qt.Unchecked)

    def delete_selected_files(self, model, directory):
        # UI_6App의 기능을 그대로 유지합니다.
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]
        for item in selected_items:
            file_path = os.path.join(directory, item.text())
            try:
                os.remove(file_path)
                model.removeRow(item.row())
            except OSError as e:
                print(f"Failed to delete {item.text()}: {str(e)}")

    @Slot()
    def run_labeling_tool(self):
        file_base_path, _ = os.path.splitext(self.selected_file_path)
        file_name = os.path.basename(file_base_path)
        bbox_path = os.path.join('app', 'gui', 'SampleRepo', file_name, file_name + '_privacy_bbox.txt')
        self.labeling_tool_window = LabelingTool(self.selected_file_path, bbox_path)
        self.labeling_tool_window.show()

    @Slot()
    def close_ui_6_and_open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
        
    @Slot()
    def close_ui_6_and_open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_6_and_open_ui_3(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()


    @Slot("QModelIndex")
    def display_image_preview(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item is not None:
            file_name = item.text()
            file_path = os.path.join(self.current_dir, 'down', file_name)
            self.selected_file_path = file_path
            
            pixmap = QPixmap(file_path)
            target_width = 281
            target_height = 351
            scaled_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
            self.ui.label_6.setPixmap(scaled_pixmap)

    def show_folder_contents(self, model, directory, index):
        item = model.itemFromIndex(index)
        folder_path = os.path.join(directory, item.text())
        print(folder_path)
        folder_path2 = os.path.join(folder_path, 'Upload')
        print(folder_path2)
        
        if os.path.isdir(folder_path):
            if not os.path.exists(folder_path2):
                os.makedirs(folder_path2)

            self.show_file_list(folder_path2)
            self.ui_8_window = UI_8App(folder_path2)
            self.ui_8_window.show()
            self.close()
        else:
            print(f"{folder_path}은(는) 폴더가 아닙니다.")

class UI_8App(QMainWindow):
    def __init__(self, directory):
        super(UI_8App, self).__init__()
        self.ui = Ui_MainWindow8()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.current_dir = directory
        self.show_file_list(self.current_dir)
        
        self.ui.label_2.setText(os.path.basename(directory))
        self.ui.pushButton_3.clicked.connect(self.close_ui_8_and_open_ui_6)
        self.ui.pushButton_2.clicked.connect(self.close_ui_8_and_open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.close_ui_8_and_open_ui_6)
        self.ui.pushButton_9.clicked.connect(self.close_ui_8_and_open_ui_3)
        self.ui.pushButton_4.clicked.connect(self.perform_sample)
        
    def get_selected_file_name(self):
        model = self.ui.listView.model()
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        if selected_items:
            file_name = selected_items[0].text()
            directory = os.path.join(self.current_dir)  # 또는 원하는 디렉토리로 수정
            file_path = os.path.join(directory, file_name)
            return file_path
        else:
            return None

    def show_file_list(self, directory):
        file_list = os.listdir(directory)
        self.model.clear()

        for item_text in file_list:
            item = CheckableItem(item_text)
            self.model.appendRow(item)
        
        self.ui.listView.setModel(self.model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(self.model, directory))
        self.ui.pushButton_8.clicked.connect(self.upload_file)
        
    def upload_file(self):
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(self, "파일 선택", "", "모든 파일 (*);;텍스트 파일 (*.txt);;이미지 파일 (*.png *.jpg)")

        for file_path in file_paths:
        # 복사될 파일의 목적지 경로
            destination_path = os.path.join(self.current_dir, os.path.basename(file_path))

            try:
                # 파일을 목적지 경로로 복사
                shutil.copy(file_path, destination_path)
                item = CheckableItem(os.path.basename(destination_path))
                self.model.appendRow(item)
            except Exception as e:
                print(f"파일 업로드 중 오류 발생: {str(e)}")
                
        self.ui.listView.setModel(self.model)

    @Slot()
    def run_predict_process(self):
        selected_file_name = self.get_selected_file_name()

        if selected_file_name:
            other_directory = os.path.join(self.current_dir, '..', 'Model')
            predict_process_path = os.path.join(other_directory, 'predictProcess.py')
            function_name = 'ser_re'  # 'ser' 또는 'ser_re' 중 선택

            try:
                base_name = os.path.basename(selected_file_name)
                file_name, _ = os.path.splitext(base_name)

                # SampleRepo, Results, SampleRepo/이미지파일명, Results/이미지파일명 폴더 생성
                for dir_name in ['SampleRepo', 'Results']:
                    dir_path = os.path.join('app', 'gui', dir_name)
                    specific_dir_path = os.path.join(dir_path, file_name)

                    for path in [dir_path, specific_dir_path]:
                        if not os.path.exists(path):
                            os.makedirs(path)

                # 입력받은 파일을 SampleRepo/이미지파일명 내부에 복사
                sample_repo_dir = os.path.join('app', 'gui', 'SampleRepo', file_name)
                shutil.copy2(selected_file_name, sample_repo_dir)

                subprocess.run(["python", predict_process_path, function_name, selected_file_name])

            except Exception as e:
                print(f"An error occurred: {e}")


    def perform_sample(self):
        current_dir = self.current_dir
        selected_file_dir = self.get_selected_file_name()
        script_path = os.path.join("app", "Model", "SampleProcess.py")
        subprocess.run(["python", script_path, current_dir, selected_file_dir])
        
        # SER 작업 수행
        #selected_file_name = self.get_selected_file_name()
        #print(selected_file_name)
        #script_path = os.path.join("app", "Model", "predictProcess.py")
        #subprocess.run(["python", script_path, "ser", self.current_dir])

    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            # 선택한 항목의 파일 경로
            file_path = os.path.join(directory, item.text())

            try:
                os.remove(file_path)  # 파일 삭제
                model.removeRow(item.row())  # 모델에서 항목 제거
            except OSError as e:
                print(f"Failed to delete {item.text()}: {str(e)}")
        
    @Slot()
    def close_ui_8_and_open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_8_and_open_ui_6(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()
    
    @Slot()
    def close_ui_8_and_open_ui_3(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # UI_2App 인스턴스를 생성하여 처음 화면으로 보여줍니다.
    ui2_window = UI_2App()
    ui2_window.show()

    sys.exit(app.exec())
