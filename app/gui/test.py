import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from PySide6.QtCore import QDir, Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow

class CheckableItem(QStandardItem):
    def __init__(self, text):
        super(CheckableItem, self).__init__(text)
        self.setCheckable(True)
        self.setCheckState(Qt.Unchecked)  # 초기 상태를 Unchecked로 설정

class UI_1App(QMainWindow):
    def __init__(self):
        super(UI_1App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.listView.setEditTriggers(QListView.NoEditTriggers)  # 읽기 전용으로 설정
        self.ui.listView.setSelectionMode(QListView.MultiSelection)  # 다중 선택 모드 설정

        self.show_file_list()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI_1App()
    window.show()
    sys.exit(app.exec_())
