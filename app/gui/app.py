import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog
from PySide6.QtCore import QDir, Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2
from ui_3 import Ui_MainWindow3
from ui_4 import Ui_MainWindow4

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
        # pushButton_2 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_2.clicked.connect(self.open_ui_4)

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

class UI_4App(QMainWindow):
    def __init__(self):
        super(UI_4App, self).__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)

        # pushButton 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton.clicked.connect(self.close_ui_4_and_open_ui_1)
        # pushButton_3 클릭 이벤트에 대한 핸들러를 연결합니다.
        self.ui.pushButton_3.clicked.connect(self.close_ui_4_and_open_ui_2)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # UI_2App 인스턴스를 생성하여 처음 화면으로 보여줍니다.
    ui2_window = UI_2App()
    ui2_window.show()

    sys.exit(app.exec_())
