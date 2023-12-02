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
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2
from ui_3 import Ui_MainWindow3
from ui_4 import Ui_MainWindow4
from ui_6 import Ui_MainWindow6
from ui_7 import Ui_MainWindow7
from ui_8 import Ui_MainWindow8

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

class CheckableItem(QStandardItem):
    def __init__(self, text, is_folder=False):
        super(CheckableItem, self).__init__(text)
        self.is_folder = is_folder
        self.setCheckable(True)
        self.setCheckState(Qt.Unchecked)

class UI_1App(QMainWindow):
    def __init__(self):
        super(UI_1App, self).__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)
        self.selected_directory = ""  # Initialize the selected directory variable

        self.ui.listView.setEditTriggers(QListView.NoEditTriggers)
        self.ui.listView.setSelectionMode(QListView.MultiSelection)

        # pushButton_5 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_5.clicked.connect(self.select_directory)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.open_ui_2)
        # pushButton_2 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.open_ui_6)
        self.ui.pushButton_7.clicked.connect(self.open_ui_7)
        self.ui.pushButton_8.clicked.connect(self.open_ui_3)
        self.ui.pushButton_4.clicked.connect(self.save_files)
        self.default_save_directory = os.path.join(script_directory, 'down')


    def show_file_list(self, directory):
        model = QStandardItemModel()

    # 현재 디렉토리 내의 파일 목록을 가져옵니다.
        file_list = os.listdir(directory)

        for item_text in file_list:
            item_path = os.path.join(directory, item_text)
            is_folder = os.path.isdir(item_path)

            if is_folder or item_text.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf', '.txt')):
                item = CheckableItem(item_text, is_folder)
                model.appendRow(item)

        self.ui.listView.setModel(model)

    def get_save_directory(self):
        return self.selected_directory

    @Slot()
    def save_files(self):
        if not self.selected_directory:
            QMessageBox.information(self, "알림", "디렉토리를 선택하세요.")
            return

        save_directory = self.default_save_directory

        # 모델에서 체크된 아이템을 가져옵니다.
        model = self.ui.listView.model()
        checked_items = [model.item(row) for row in range(model.rowCount()) if model.item(row).checkState() == Qt.Checked]

        if not checked_items:
            QMessageBox.information(self, "알림", "선택된 파일이 없습니다.")
            return

        try:
            os.makedirs(save_directory, exist_ok=True)  # 디렉토리가 존재하지 않으면 생성
        except Exception as e:
            QMessageBox.critical(self, "오류", f"디렉토리 생성 중 오류가 발생했습니다: {str(e)}")
            return

        # 체크된 아이템을 복사합니다.
        for item in checked_items:
            file = item.text()
            source_path = os.path.join(self.selected_directory, file)
            destination_path = os.path.join(save_directory, file)

            try:
                shutil.copy(source_path, destination_path)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 저장하는 중 오류가 발생했습니다: {str(e)}")
                return

        QMessageBox.information(self, "알림", "선택한 파일이 저장되었습니다.")


    @Slot()
    def select_directory(self):
        self.selected_directory = QFileDialog.getExistingDirectory(self, "디렉토리 선택", QDir.currentPath())

        if self.selected_directory:
            self.show_file_list(self.selected_directory)

    @Slot()
    def open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()

    @Slot()
    def open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
        
    @Slot()
    def open_ui_6(self):
        # pushButton_6를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()
    
    @Slot()
    def open_ui_7(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_7_window = UI_7App()
        self.ui_7_window.show()
        self.close()
    
    @Slot()
    def open_ui_3(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()

class UI_2App(QMainWindow):
    def __init__(self):
        super(UI_2App, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        # pushButton 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton.clicked.connect(self.close_ui_2_and_open_ui_1)
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.close_ui_2_and_open_ui_4)
        # pushButton_3클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_4.clicked.connect(self.close_ui_2_and_open_ui_3)
        self.ui.pushButton_6.clicked.connect(self.close_ui_2_and_open_ui_6)

    @Slot()
    def close_ui_2_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

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
        # pushButton 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton.clicked.connect(self.close_ui_3_and_open_ui_1)
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.close_ui_3_and_open_ui_4)
        # pushButton_2클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_3_and_open_ui_2)
        self.ui.pushButton_6.clicked.connect(self.close_ui_3_and_open_ui_6)
        self.ui.pushButton_7.clicked.connect(self.close_ui_3_and_open_ui_7)
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
    def close_ui_3_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

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
    
    @Slot()
    def close_ui_3_and_open_ui_7(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_7_window = UI_7App()
        self.ui_7_window.show()
        self.close()

class UI_4App(QMainWindow):
    def __init__(self):
        super(UI_4App, self).__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)

        # pushButton 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton.clicked.connect(self.close_ui_4_and_open_ui_1)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_4_and_open_ui_2)
        # pushButton_6 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_6.clicked.connect(self.close_ui_4_and_open_ui_6)
        self.ui.pushButton_7.clicked.connect(self.close_ui_4_and_open_ui_7)
        self.ui.pushButton_8.clicked.connect(self.close_ui_4_and_open_ui_3)

    @Slot()
    def close_ui_4_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

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
    def close_ui_4_and_open_ui_7(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_7_window = UI_7App()
        self.ui_7_window.show()
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
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close_ui_6_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_6_and_open_ui_2)
        self.ui.pushButton_2.clicked.connect(self.close_ui_6_and_open_ui_4)
        self.ui.pushButton_7.clicked.connect(self.close_ui_6_and_open_ui_7)
        self.ui.pushButton_8.clicked.connect(self.close_ui_6_and_open_ui_3)
        self.ui.pushButton_4.clicked.connect(self.run_labeling_tool)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SampleRepo')
        self.show_file_list(directory)

        self.selected_file_path = ""
        
    def show_file_list(self, directory):
    # 선택한 디렉토리 내의 파일 목록을 가져옵니다.
        file_list = os.listdir(directory)

        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)
            
        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.listView.clicked.connect(self.display_image_preview)

    # itemChanged 시그널을 처리하는 슬롯
    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        if item.checkState() == Qt.Checked:
            # 아이템이 체크될 때 다른 모든 아이템의 체크를 해제
            model = item.model()
            for row in range(model.rowCount()):
                if model.item(row) != item:
                    model.item(row).setCheckState(Qt.Unchecked)
    
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
    def run_labeling_tool(self):
        file_base_path, _ = os.path.splitext(self.selected_file_path)
        file_name = os.path.basename(file_base_path)
        bbox_path = os.path.join('app', 'gui', 'SampleRepo', file_name, file_name + '_privacy_bbox.txt')
        self.labeling_tool_window = LabelingTool(self.selected_file_path, bbox_path)
        self.labeling_tool_window.show()

    @Slot()
    def close_ui_6_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

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
    def close_ui_6_and_open_ui_7(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_7_window = UI_7App()
        self.ui_7_window.show()
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
    # 항목이 클릭될 때 선택한 파일 경로를 업데이트
        item = self.ui.listView.model().itemFromIndex(index)
        if item is not None:
            file_name = item.text()
            file_path = os.path.join(self.current_dir, 'down', file_name)
            self.selected_file_path = file_path
            
        # 미리보기 업데이트 코드 추가
        pixmap = QPixmap(file_path)
        # 이미지 크기 조절
        target_width = 281
        target_height = 351
        scaled_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
        self.ui.label_6.setPixmap(scaled_pixmap)
        
class UI_7App(QMainWindow):
    def __init__(self):
        super(UI_7App, self).__init__()
        self.ui = Ui_MainWindow7()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close_ui_7_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_7_and_open_ui_2)
        self.ui.pushButton_2.clicked.connect(self.close_ui_7_and_open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.close_ui_7_and_open_ui_6)
        self.ui.pushButton_8.clicked.connect(self.close_ui_7_and_open_ui_3)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SampleRepo')
        self.show_file_list(directory)

        self.selected_file_path = ""
        
    def show_file_list(self, directory):
    # 선택한 디렉토리 내의 파일 목록을 가져옵니다.
        file_list = os.listdir(directory)

        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.listView.doubleClicked.connect(lambda index: self.show_folder_contents(model, directory, index))
        
    def show_folder_contents(self, model, directory, index):
        item = model.itemFromIndex(index)
        folder_path = os.path.join(directory, item.text())

        if os.path.isdir(folder_path):
            # 선택한 폴더 내의 파일 목록을 가져와서 ListView에 출력
            self.show_file_list_in_ui_8(folder_path)
        else:
            print(f"{folder_path}은(는) 폴더가 아닙니다.")
    
    def show_file_list_in_ui_8(self, directory):
        self.ui_8_window = UI_8App(directory)
        self.ui_8_window.show()
        self.close()

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
    def close_ui_7_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_7_and_open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
        
    @Slot()
    def close_ui_7_and_open_ui_4(self):
        # pushButton_2를 클릭했을 때 실행될 함수입니다.
        # UI_4App 인스턴스를 생성하여 UI_4 화면으로 전환합니다.
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_7_and_open_ui_6(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()
    
    @Slot()
    def close_ui_7_and_open_ui_3(self):
        # pushButton_7를 클릭했을 때 실행될 함수입니다.
        # UI_7App 인스턴스를 생성하여 UI_7 화면으로 전환합니다.
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
        
class UI_8App(QMainWindow):
    def __init__(self, directory):
        super(UI_8App, self).__init__()
        self.ui = Ui_MainWindow8()
        self.ui.setupUi(self)
        self.model = QStandardItemModel()
        self.current_dir = directory
        self.show_file_list(self.current_dir)
        
        self.ui.label_2.setText(os.path.basename(directory))
        self.ui.pushButton.clicked.connect(self.close_ui_8_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_8_and_open_ui_7)
        self.ui.pushButton_7.clicked.connect(self.close_ui_8_and_open_ui_7)
        self.ui.pushButton_2.clicked.connect(self.close_ui_8_and_open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.close_ui_8_and_open_ui_6)
        self.ui.pushButton_9.clicked.connect(self.close_ui_8_and_open_ui_3)
        self.ui.pushButton_4.clicked.connect(self.perform_ser)

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

    def perform_ser(self):
        # SER 작업 수행
        script_path = os.path.join("app", "Model", "predictProcess.py")
        subprocess.run(["python", script_path, "ser", self.current_dir])

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
    def close_ui_8_and_open_ui_1(self):
        # pushButton를 클릭했을 때 실행될 함수입니다.
        # UI_1App 인스턴스를 생성하여 UI_1 화면으로 전환합니다.
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_8_and_open_ui_7(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # UI_2App 인스턴스를 생성하여 UI_2 화면으로 전환합니다.
        self.ui_7_window = UI_7App()
        self.ui_7_window.show()
        self.close()
        
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
