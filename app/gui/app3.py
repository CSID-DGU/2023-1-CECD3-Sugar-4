import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton
from PySide6.QtCore import QDir, Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2  # ui_2 모듈을 가져옵니다.

# CheckableItem 및 UI_1App 클래스는 이전과 동일하게 유지됩니다.
class CheckableItem(QStandardItem):
    def __init__(self, text):
        super(CheckableItem, self).__init__(text)
        self.setCheckable(True)
        self.setCheckState(Qt.Unchecked)  # 초기 상태를 Unchecked로 설정
        
class UI_1App(QMainWindow):
    def __init__(self):
        super(UI_1App, self).__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        self.ui.listView.setEditTriggers(QListView.NoEditTriggers)
        self.ui.listView.setSelectionMode(QListView.MultiSelection)

        self.show_file_list()

        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.open_ui_2)

    def show_file_list(self):
        current_directory = QDir.currentPath()
        file_list = os.listdir(current_directory)

        # 디렉터리 및 파일을 리스트로 필터링합니다.
        file_list = [item for item in file_list if os.path.isdir(item) or os.path.isfile(item)]

        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)

    @Slot()
    def open_ui_2(self):
        # pushButton_3를 클릭했을 때 실행될 함수입니다.
        # ui_2를 실행하는 코드를 추가합니다.
        self.ui_2_window = QMainWindow()
        self.ui_2 = Ui_MainWindow2()
        self.ui_2.setupUi(self.ui_2_window)

        # pushButton4 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui_2.pushButton_4.clicked.connect(self.close_ui_2_and_open_ui_1)

        self.ui_2_window.show()
        self.close()

    def close_ui_2_and_open_ui_1(self):
        # pushButton4를 클릭했을 때 실행될 함수입니다.
        # ui_2를 닫고 ui_1을 다시 표시합니다.
        self.ui_2_window.close()
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI_1App()
    window.show()
    sys.exit(app.exec_())