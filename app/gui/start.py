import subprocess
import sys
from pathlib import Path
current_path = Path(__file__).resolve().parent
sys.path.append(str(current_path / 'UI'))

from enum import Enum
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import QDir, Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2
from ui_3 import Ui_MainWindow3
from ui_4 import Ui_MainWindow4
from ui_6 import Ui_MainWindow6

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
        self.ui.pushButton_4.clicked.connect(self.run_predict_process)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
# Set the directory to a relative path within the script's directory
        directory = os.path.join(script_directory, 'down')

        self.show_file_list(directory)


    def show_file_list(self, directory):
    # 선택한 디렉토리 내의 파일 목록을 가져옵니다.
        file_list = os.listdir(directory)

    # 모든 파일을 필터링합니다.
        filtered_files = file_list

        model = QStandardItemModel()
        for item_text in filtered_files:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))

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
            # 다른 디렉토리에 있는 predictProcess.py의 run_ser_prediction 실행
            other_directory = os.path.join(self.current_dir, '..', 'Model')
            predict_process_path = os.path.join(other_directory, 'predictProcess.py')

            try:
                subprocess.run(["python", predict_process_path, selected_file_name])
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

class UI_6App(QMainWindow):
    def __init__(self):
        super(UI_6App, self).__init__()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)

        # pushButton 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton.clicked.connect(self.close_ui_6_and_open_ui_1)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_6_and_open_ui_2)
        # pushButton_2 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.close_ui_6_and_open_ui_4)
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # Set the directory to a relative path within the script's directory
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'output')
        self.show_file_list(directory)
        
    def show_file_list(self, directory):
    # 선택한 디렉토리 내의 파일 목록을 가져옵니다.
        file_list = os.listdir(directory)

    # 모든 파일을 필터링합니다.
        filtered_files = file_list

        model = QStandardItemModel()
        for item_text in filtered_files:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        
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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # UI_2App 인스턴스를 생성하여 처음 화면으로 보여줍니다.
    ui2_window = UI_2App()
    ui2_window.show()

    sys.exit(app.exec())
