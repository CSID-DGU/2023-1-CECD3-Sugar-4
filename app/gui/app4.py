import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog
from PySide6.QtCore import QDir, Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2

class CheckableItem(QStandardItem):
    def __init__(self, text):
        super(CheckableItem, self).__init__(text)
        self.setCheckable(True)
        self.setCheckState(Qt.Unchecked)

class UI_1App(QMainWindow):
    def __init__(self):
        super(UI_1App, self).__init__()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self)

        self.ui.listView.setEditTriggers(QListView.NoEditTriggers)
        self.ui.listView.setSelectionMode(QListView.MultiSelection)

        # pushButton_5 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_5.clicked.connect(self.select_directory)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.open_ui_2)

    def show_file_list(self, directory):
        file_list = os.listdir(directory)

        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)

    @Slot()
    def select_directory(self):
        # pushButton_5를 클릭했을 때 실행될 함수입니다.
        # 사용자에게 디렉토리를 선택하도록 대화 상자를 엽니다.
        selected_directory = QFileDialog.getExistingDirectory(self, "디렉토리 선택", QDir.currentPath())

        if selected_directory:
            # 사용자가 디렉토리를 선택한 경우 선택한 디렉토리의 파일 목록을 표시합니다.
            self.show_file_list(selected_directory)

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
