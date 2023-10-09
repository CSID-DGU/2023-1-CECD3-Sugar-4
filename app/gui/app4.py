import sys
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog, QMessageBox
from PySide6.QtCore import QDir, Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_1 import Ui_MainWindow1
from ui_2 import Ui_MainWindow2

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
        self.ui.listView.clicked.connect(self.toggle_item_check_state)
        self.ui.pushButton_5.clicked.connect(self.select_directory)
        self.ui.pushButton_3.clicked.connect(self.open_ui_2)
        self.ui.pushButton_4.clicked.connect(self.save_files)
        self.default_save_directory = "C:\\Users\\USER\\GUI\\pyside gui\\venv"


    def show_file_list(self, directory):
        model = QStandardItemModel()

        for root, dirs, files in os.walk(directory):
            for item_text in dirs + files:
                item_path = os.path.join(root, item_text)
                is_folder = os.path.isdir(item_path)

                if is_folder or item_text.lower().endswith(('.png', '.jpg', '.jpeg')):
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

        # Check if any file is selected
        if not self.ui.listView.selectedIndexes():
            QMessageBox.information(self, "알림", "저장할 파일을 선택하세요.")
            return

        selected_indexes = self.ui.listView.selectedIndexes()
        selected_files = [self.ui.listView.model().itemFromIndex(index).text() for index in selected_indexes]

        for file in selected_files:
            source_path = os.path.join(self.selected_directory, file)
            destination_path = os.path.join(save_directory, file)

            try:
                shutil.copy(source_path, destination_path)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 저장하는 중 오류가 발생했습니다: {str(e)}")
                return

        QMessageBox.information(self, "알림", "파일이 저장되었습니다.")
    @Slot()
    def select_directory(self):
        self.selected_directory = QFileDialog.getExistingDirectory(self, "디렉토리 선택", QDir.currentPath())

        if self.selected_directory:
            self.show_file_list(self.selected_directory)

    @Slot()
    def open_ui_2(self):
        self.ui_2_window = QMainWindow()
        self.ui_2 = Ui_MainWindow2()
        self.ui_2.setupUi(self.ui_2_window)

        self.ui_2.pushButton_4.clicked.connect(self.close_ui_2_and_open_ui_1)

        self.ui_2_window.show()
        self.close()

    def close_ui_2_and_open_ui_1(self):
        self.ui_2_window.close()
        self.show()

    def toggle_item_check_state(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item.isCheckable():
            item.setCheckState(Qt.Checked if item.checkState() == Qt.Unchecked else Qt.Unchecked)
            self.ui.listView.model().itemChanged.emit(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI_1App()
    window.show()
    sys.exit(app.exec())