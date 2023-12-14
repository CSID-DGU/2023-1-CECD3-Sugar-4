import subprocess
import sys
import re
import cv2
from pathlib import Path
import app
current_path = Path(__file__).resolve().parent
sys.path.append(str(current_path / 'UI'))

from app import mask_image_with_bboxes
from app import LabelingToolByNewImage, LabelingToolBySampleImage

##from app.gui.UI.ui_1 import ui_1, ui_2, ui_3, ui_4, ui_5, ui_6, ui_7, ui_8, ui_help
from app.gui.UI.ui_1 import Ui_MainWindow1
from app.gui.UI.ui_2 import Ui_MainWindow2
from app.gui.UI.ui_3 import Ui_MainWindow3
from app.gui.UI.ui_4 import Ui_MainWindow4
from app.gui.UI.ui_5 import Ui_MainWindow5
from app.gui.UI.ui_6 import Ui_MainWindow6
from app.gui.UI.ui_7 import Ui_MainWindow7
from app.gui.UI.ui_8 import Ui_MainWindow8
from app.gui.UI.ui_help import Ui_MainWindowhelp

from enum import Enum
import os
import shutil
import subprocess
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QPushButton, QFileDialog, QMessageBox, QLabel, QVBoxLayout, QWidget, QListWidget, QCheckBox
from PySide6.QtCore import QDir, Qt, Slot, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap

abc = os.path.dirname(os.path.abspath(app.__file__))
script_directory = os.path.join(abc, '..')

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
        self.setFixedSize(1040, 600)
        self.ui.pushButton_3.clicked.connect(self.close_ui_1_and_open_ui_2)
        self.ui.pushButton_8.clicked.connect(self.close_ui_1_and_open_ui_3)
        self.ui.pushButton_6.clicked.connect(self.close_ui_1_and_open_ui_4)
        self.ui.pushButton.clicked.connect(self.close_ui_1_and_open_ui_6)
        self.ui.checkBox.stateChanged.connect(self.handle_stateChanged)
        self.show_file_dictionary(os.path.join(script_directory,'app', 'gui', 'Results'))
        self.ui.pushButton_4.clicked.connect(self.download_files)
        self.ui.listView.doubleClicked.connect(self.handle_listview_doubleclick)
        self.checked_item = ""
        self.folder_item = ""
        
    def handle_stateChanged(self, state):
        model = self.ui.listView.model()
        check_state = Qt.CheckState(state)

        for row in range(model.rowCount()):
            item = model.item(row)
            item.setCheckState(check_state)
            
    def show_file_list(self, directory):
        file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.endswith('.txt')]
        model = QStandardItemModel()

        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.listView.clicked.connect(self.display_image_preview)
        self.ui.checkBox.stateChanged.connect(self.handle_stateChanged)
        
    def reopen_ui(self):
        """ 현재 UI를 닫고 새로운 UI_1App 인스턴스를 연다 """
        self.close()
        self.new_instance = UI_1App()
        self.new_instance.show()
        
    @Slot("QModelIndex")
    def display_image_preview(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item is not None:
            file_name = item.text()
            file_path = os.path.join(script_directory, 'app', 'gui', 'Results', self.folder_item, file_name)
            self.selected_file_path = file_path
            
            pixmap = QPixmap(file_path)
            target_width = 281
            target_height = 351
            scaled_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
            self.ui.label_6.setPixmap(scaled_pixmap)
            
    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        if item.checkState() == Qt.Checked:
            model = self.ui.listView.model()
        self.checked_item = item.text()

    def custom_copy(self, src, dst):
            """ .txt 파일을 제외하고 복사하는 사용자 정의 함수 """
            if not src.endswith('.txt'):
                shutil.copy2(src, dst)

    def download_files(self):
        download_folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if download_folder:
            model = self.ui.listView.model()
            selected_items = [model.item(i).text() for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

            for item_text in selected_items:
                source_path = os.path.join(script_directory, 'app/gui/Results', self.folder_item, item_text)
                destination_path = os.path.join(download_folder, item_text)

                try:
                    if os.path.isfile(source_path):
                        shutil.copy2(source_path, destination_path)
                    elif os.path.isdir(source_path):
                        shutil.copytree(source_path, destination_path, copy_function=self.custom_copy)

                    QMessageBox.information(self,"알림","파일이 다운로드 되었습니다.")
                    self.reopen_ui()
                except OSError as e:
                    print(f"Failed to move {item_text}: {str(e)}")
                    QMessageBox.information(self,"알림","파일이 다운로드에 실패하였습니다.")

    def show_file_dictionary(self, directory):
        file_list = os.listdir(directory)
        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)
        
        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.listView.doubleClicked.connect(self.handle_listview_doubleclick)
        self.ui.listView.clicked.connect(self.display_image_preview)
    
    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            file_path = os.path.join(directory, item.text())

            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    model.removeRow(item.row())
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    model.removeRow(item.row())
                QMessageBox.information(self,"알림","파일이 제거 되었습니다.")
            except OSError as e:
                print(f"{item.text()} 삭제 실패: {str(e)}")
                QMessageBox.information(self,"알림","파일 제거에 실패하였습니다.")

    @Slot("QModelIndex")
    def handle_listview_doubleclick(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item and os.path.isdir(os.path.join(script_directory, 'app/gui/Results', item.text())):
            self.folder_item = item.text()
            self.show_file_list(os.path.join(script_directory, 'app/gui/Results', item.text()))
            
    @Slot()
    def close_ui_1_and_open_ui_2(self):
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()

    @Slot()
    def close_ui_1_and_open_ui_3(self):
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
    
    @Slot()    
    def close_ui_1_and_open_ui_4(self):
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_1_and_open_ui_6(self):
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()
        
class UI_2App(QMainWindow):
    def __init__(self):
        super(UI_2App, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.setFixedSize(1040, 600)
        self.ui.pushButton.clicked.connect(self.close_ui_2_and_open_ui_help)
        self.ui.pushButton_7.clicked.connect(self.close_ui_2_and_open_ui_1)
        self.ui.pushButton_4.clicked.connect(self.close_ui_2_and_open_ui_3)
        self.ui.pushButton_2.clicked.connect(self.close_ui_2_and_open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.close_ui_2_and_open_ui_6)
    
    @Slot()
    def close_ui_2_and_open_ui_help(self):
        self.ui_help_window = UI_helpApp()
        self.ui_help_window.show()
        self.close()
        
    @Slot()
    def close_ui_2_and_open_ui_1(self):
        try:
            self.ui_1_window = UI_1App()
            self.ui_1_window.show()
            self.close()
        except:
            QMessageBox.critical(self,"오류","개인정보 자동 인식을 먼저 시도하세요.")

    @Slot()
    def close_ui_2_and_open_ui_3(self):
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()

    @Slot()
    def close_ui_2_and_open_ui_4(self):
        try:
            self.ui_4_window = UI_4App()
            self.ui_4_window.show()
            self.close()
        except:
            QMessageBox.critical(self,"오류","개인정보 자동 인식을 먼저 시도하세요.")
        
    @Slot()
    def close_ui_2_and_open_ui_6(self):
        try:
            self.ui_6_window = UI_6App()
            self.ui_6_window.show()
            self.close()
        except:
            QMessageBox.critical(self,"오류","개인정보 자동 인식을 먼저 시도하세요.")

class UI_3App(QMainWindow):
    def __init__(self):
        super(UI_3App, self).__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.setFixedSize(1040, 600)
        self.model = QStandardItemModel()
        self.ui.pushButton_7.clicked.connect(self.close_ui_3_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_3_and_open_ui_2)
        self.ui.pushButton_2.clicked.connect(self.close_ui_3_and_open_ui_4)
        self.ui.pushButton_6.clicked.connect(self.close_ui_3_and_open_ui_6)
        self.ui.pushButton_4.clicked.connect(self.run_predict_process)
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(script_directory, 'app', 'gui', 'down')
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.show_file_list(directory)

    def show_file_list(self, directory):
        file_list = os.listdir(directory)
        filtered_files = file_list

        model = QStandardItemModel()
        for item_text in filtered_files:
            item = CheckableItem(item_text)
            model.appendRow(item)

        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_5.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.pushButton_9.clicked.connect(self.upload_file)
        self.model=model
        
    def upload_file(self):
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(self, "파일 선택", "", "모든 파일 (*);;텍스트 파일 (*.txt);;이미지 파일 (*.png *.jpg)")
        destination_directory = os.path.join(script_directory, 'app', 'gui', 'down')

        for file_path in file_paths:
            destination_path = os.path.join(destination_directory, os.path.basename(file_path))

            try:
                shutil.copy(file_path, destination_path)
                item = CheckableItem(os.path.basename(destination_path))
                self.model.appendRow(item)
                QMessageBox.information(self,"알림","파일이 업로드 되었습니다.")
            except Exception as e:
                print(f"파일 업로드 중 오류 발생: {str(e)}")
                QMessageBox.information(self,"오류","파일이 업로드 되지 않았습니다.")
        
    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        if item.checkState() == Qt.Checked:
            model = item.model()
            for row in range(model.rowCount()):
                if model.item(row) != item:
                    model.item(row).setCheckState(Qt.Unchecked)

    def get_selected_file_name(self):
        model = self.ui.listView.model()
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        if selected_items:
            file_name = selected_items[0].text()
            directory = os.path.join(script_directory, 'app','gui', 'down')
            file_path = os.path.join(directory, file_name)
            return file_path
        else:
            return None

    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            file_path = os.path.join(directory, item.text())

            try:
                os.remove(file_path)
                model.removeRow(item.row())
                QMessageBox.information(self,"알림","파일이 제거 되었습니다.")
            except OSError as e:
                print(f"Failed to delete {item.text()}: {str(e)}")
                QMessageBox.information(self,"알림","파일 제거에 실패하였습니다.")

    @Slot()
    def run_predict_process(self):
        selected_file_name = self.get_selected_file_name()

        if selected_file_name:
            other_directory = os.path.join(script_directory, 'app', 'Model')
            predict_process_path = os.path.join(other_directory, 'predictProcess.py')
            function_name = 'ser_re'

            try:
                base_name = os.path.basename(selected_file_name)
                file_name, _ = os.path.splitext(base_name)

                for dir_name in ['SampleRepo', 'Results']:
                    dir_path = os.path.join(script_directory, 'app', 'gui', dir_name)
                    specific_dir_path = os.path.join(dir_path, file_name)

                    for path in [dir_path, specific_dir_path]:
                        if not os.path.exists(path):
                            os.makedirs(path)

                sample_repo_dir = os.path.join(script_directory, 'app', 'gui', 'SampleRepo', file_name)
                shutil.copy2(selected_file_name, sample_repo_dir)
                subprocess.run(["python3", predict_process_path, function_name, selected_file_name])
                QMessageBox.information(self,"알림","개인정보 자동 인식이 완료되었습니다.\n샘플 문서 목록에서 마스킹을 진행하세요.")

            except Exception as e:
                print(f"An error occurred: {e}")

        file_name = os.path.basename(specific_dir_path)
        file_path = os.path.join(script_directory, 'app', 'gui', 'SampleRepo', file_name)
        bbox_path = os.path.join(file_path, file_name + '_privacy_bbox.txt')
        image_path = self.get_selected_file_name()
        image_directory_path = os.path.join(file_path, os.path.basename(selected_file_name))
        self.labeling_tool_window = LabelingToolByNewImage(image_path, image_directory_path, bbox_path)
        self.labeling_tool_window.show()
                
    @Slot()
    def close_ui_3_and_open_ui_1(self):
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_3_and_open_ui_2(self):
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()        

    @Slot()
    def close_ui_3_and_open_ui_4(self):
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_3_and_open_ui_6(self):
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

class UI_4App(QMainWindow):
    def __init__(self):
        super(UI_4App, self).__init__()
        self.ui = Ui_MainWindow4()
        self.ui.setupUi(self)
        self.setFixedSize(1040, 600)
        self.ui.pushButton_7.clicked.connect(self.close_ui_4_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_4_and_open_ui_2)
        self.ui.pushButton_8.clicked.connect(self.close_ui_4_and_open_ui_3)
        self.ui.pushButton_6.clicked.connect(self.close_ui_4_and_open_ui_6)

        self.show_file_dictionary(os.path.join(script_directory, 'app/gui/Results'))
        self.ui.listView.doubleClicked.connect(self.handle_listview_doubleclick)
        self.ui.pushButton_5.clicked.connect(self.run_labeling_tool)
        self.checked_item = ""
        self.folder_item = ""

    def show_file_list(self, directory):
        file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.endswith('.txt')]
        model = QStandardItemModel()

        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.listView.clicked.connect(self.display_image_preview)
        
    @Slot("QModelIndex")
    def display_image_preview(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item is not None:
            file_name = item.text()
            file_path = os.path.join(script_directory, 'app', 'gui', 'Results', self.folder_item, file_name)
            self.selected_file_path = file_path

            pixmap = QPixmap(file_path)
            target_width = 281
            target_height = 351
            scaled_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
            self.ui.label_6.setPixmap(scaled_pixmap)
            
    @Slot(QStandardItem)
    def handle_item_changed(self, item):
        if item.checkState() == Qt.Checked:
            model = self.ui.listView.model()
            for i in range(model.rowCount()):
                if model.item(i) != item: 
                    model.item(i).setCheckState(Qt.Unchecked)
        self.checked_item = item.text()
            
    @Slot()
    def run_labeling_tool(self):
        aa = self.folder_item
        checked_item = self.checked_item
        image_name = checked_item.replace("masked_", "")
        basename, ext = os.path.splitext(image_name)
        
        image_path = os.path.join(script_directory, 'app', 'gui', 'Results',  aa)
        image_directory_path = os.path.join(script_directory, 'app', 'gui', 'SampleRepo', aa, 'Upload', image_name)
        bbox_path = os.path.join(script_directory, 'app', 'gui', 'Results', aa, basename +'.txt')

        self.labeling_tool_window = LabelingToolBySampleImage(image_path, image_directory_path , bbox_path)
        self.labeling_tool_window.show()
        
    def show_file_dictionary(self, directory):
        file_list = os.listdir(directory)
        model = QStandardItemModel()
        for item_text in file_list:
            if os.path.isdir(os.path.join(directory, item_text)):
                item = QStandardItem(item_text)
                model.appendRow(item)
            
        model.itemChanged.connect(self.handle_item_changed)
        self.ui.listView.setModel(model)
        self.ui.pushButton_9.clicked.connect(lambda: self.delete_selected_files(model, directory))
        self.ui.listView.doubleClicked.connect(self.handle_listview_doubleclick)
        
    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]
        for item in selected_items:
            file_path = os.path.join(directory, item.text())
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    model.removeRow(item.row())
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    model.removeRow(item.row())
                QMessageBox.information(self,"알림","파일이 제거 되었습니다.")
            except OSError as e:
                print(f"{item.text()} 삭제 실패: {str(e)}")
                QMessageBox.information(self,"알림","파일 제거에 실패하였습니다.")

    @Slot("QModelIndex")
    def handle_listview_doubleclick(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item and os.path.isdir(os.path.join(script_directory, 'app/gui/Results', item.text())):
            self.folder_item = item.text()
            self.show_file_list(os.path.join(script_directory, 'app/gui/Results', item.text()))

    @Slot()
    def close_ui_4_and_open_ui_1(self):
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_4_and_open_ui_2(self):
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
        
    @Slot()
    def close_ui_4_and_open_ui_3(self):
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
        
    @Slot()
    def close_ui_4_and_open_ui_6(self):
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

class UI_6App(QMainWindow):
    def __init__(self):
        super(UI_6App, self).__init__()
        self.ui = Ui_MainWindow6()
        self.ui.setupUi(self)
        self.setFixedSize(1040, 600)
        self.ui.pushButton_7.clicked.connect(self.close_ui_6_and_open_ui_1)
        self.ui.pushButton_3.clicked.connect(self.close_ui_6_and_open_ui_2)
        self.ui.pushButton_8.clicked.connect(self.close_ui_6_and_open_ui_3)
        self.ui.pushButton_2.clicked.connect(self.close_ui_6_and_open_ui_4)
        self.ui.pushButton_4.clicked.connect(self.run_labeling_tool)

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = os.path.join(script_directory, 'app', 'gui', 'SampleRepo')
        self.show_directory_list(directory)

        self.selected_file_path = ""
        
    def show_directory_list(self, directory):
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
        if item.checkState() == Qt.Checked:
            model = item.model()
            for row in range(model.rowCount()):
                if model.item(row) != item:
                    model.item(row).setCheckState(Qt.Unchecked)

    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            file_path = os.path.join(directory, item.text())

            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    model.removeRow(item.row())
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    model.removeRow(item.row())
                QMessageBox.information(self,"알림","파일이 제거 되었습니다.")
            except OSError as e:
                print(f"{item.text()} 삭제 실패: {str(e)}")
                QMessageBox.information(self,"알림","파일 제거에 실패하였습니다.")
                
    def get_selected_file_name(self):
        model = self.ui.listView.model()
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        if selected_items:
            file_name = selected_items[0].text()
            directory = os.path.join(script_directory, 'app','gui', 'down')
            file_path = os.path.join(directory, file_name)
            return file_path
        else:
            return None

    @Slot()
    def run_labeling_tool(self):
        file_base_path, _ = os.path.splitext(self.selected_file_path)
        file_name = os.path.basename(file_base_path)
        image_path = self.get_selected_file_name()
        bbox_path = os.path.join(script_directory, 'app', 'gui', 'SampleRepo', file_name, file_name + '_privacy_bbox.txt')
        self.labeling_tool_window = LabelingToolBySampleImage(image_path, self.selected_file_path, bbox_path)
        self.labeling_tool_window.show()

    @Slot()
    def close_ui_6_and_open_ui_1(self):
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_6_and_open_ui_2(self):
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
    
    @Slot()
    def close_ui_6_and_open_ui_3(self):
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
        
    @Slot()
    def close_ui_6_and_open_ui_4(self):
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot("QModelIndex")
    def display_image_preview(self, index):
        item = self.ui.listView.model().itemFromIndex(index)
        if item is not None:
            file_name = item.text()
            file_path = os.path.join(script_directory, 'app', 'gui', 'down', file_name)
            self.selected_file_path = file_path
            
            pixmap = QPixmap(file_path)
            target_width = 281
            target_height = 351
            scaled_pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio)
            self.ui.label_6.setPixmap(scaled_pixmap)

    def show_folder_contents(self, model, directory, index):
        item = model.itemFromIndex(index)
        folder_path = os.path.join(directory, item.text())
        folder_path2 = os.path.join(folder_path, 'Upload')
        
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
        self.setFixedSize(1040, 600)
        self.model = QStandardItemModel()
        self.current_dir = directory
        self.show_file_list(self.current_dir)
        
        self.ui.label_2.setText(os.path.basename(directory))
        self.ui.pushButton_7.clicked.connect(self.close_ui_8_and_open_ui_1)
        self.ui.pushButton_9.clicked.connect(self.close_ui_8_and_open_ui_3)
        self.ui.pushButton_2.clicked.connect(self.close_ui_8_and_open_ui_4)
        self.ui.pushButton_3.clicked.connect(self.close_ui_8_and_open_ui_6)
        self.ui.pushButton_6.clicked.connect(self.close_ui_8_and_open_ui_6)
        self.ui.pushButton_4.clicked.connect(self.perform_sample)
        
    def get_selected_file_paths(self):
        model = self.ui.listView.model()
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        selected_file_paths = [item.text() for item in selected_items]

        return selected_file_paths if selected_file_paths else None

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
            destination_path = os.path.join(self.current_dir, os.path.basename(file_path))

            try:
                shutil.copy(file_path, destination_path)
                item = CheckableItem(os.path.basename(destination_path))
                self.model.appendRow(item)
                QMessageBox.information(self,"알림","파일이 업로드 되었습니다.")
            except Exception as e:
                print(f"파일 업로드 중 오류 발생: {str(e)}")
                QMessageBox.information(self,"오류","파일이 업로드 되지 않았습니다.")
                
        self.ui.listView.setModel(self.model)

    @Slot()
    def run_predict_process(self):
        selected_file_name = self.get_selected_file_name()

        if selected_file_name:
            other_directory = os.path.join(self.current_dir, '..', 'Model')
            predict_process_path = os.path.join(other_directory, 'predictProcess.py')
            function_name = 'ser_re'

            try:
                base_name = os.path.basename(selected_file_name)
                file_name, _ = os.path.splitext(base_name)
                for dir_name in ['SampleRepo', 'Results']:
                    dir_path = os.path.join(script_directory, 'app', 'gui', dir_name)
                    specific_dir_path = os.path.join(dir_path, file_name)
                    for path in [dir_path, specific_dir_path]:
                        if not os.path.exists(path):
                            os.makedirs(path)

                sample_repo_dir = os.path.join(script_directory, 'app', 'gui', 'SampleRepo', file_name)
                shutil.copy2(selected_file_name, sample_repo_dir)
                subprocess.run(["python3", predict_process_path, function_name, selected_file_name])

            except Exception as e:
                print(f"An error occurred: {e}")

    def perform_sample(self):
        current_dir = self.current_dir
        parts = current_dir.split(os.sep)
        upload_index = parts.index('Upload')  
        Results_folder = parts[upload_index - 1]    
        selected_file_list = self.get_selected_file_paths()
        save_dir = os.path.join(script_directory, 'app', 'gui', 'Results',Results_folder)
        
        for selected_file in selected_file_list :  
            selected_file_dir = os.path.join(current_dir, selected_file)
            bbox_basename, extension = os.path.splitext(selected_file)
            bbox_path = os.path.join(script_directory, 'app', 'gui', 'Results', Results_folder, bbox_basename + '.txt')
            script_path = os.path.join(script_directory, "app", "Model", "SampleProcess.py")
            subprocess.run(["python3", script_path, current_dir, selected_file_dir])
            mask_image_with_bboxes(bbox_path, selected_file_dir, save_dir)
        
        QMessageBox.information(self,"알림","마스킹 작업이 완료되었습니다.")
        
            
        # SER 작업 수행
        #selected_file_name = self.get_selected_file_name()
        #print(selected_file_name)
        #script_path = os.path.join("app", "Model", "predictProcess.py")
        #subprocess.run(["python3", script_path, "ser", self.current_dir])

    def delete_selected_files(self, model, directory):
        selected_items = [model.item(i) for i in range(model.rowCount()) if model.item(i).checkState() == Qt.Checked]

        for item in selected_items:
            file_path = os.path.join(directory, item.text())

            try:
                os.remove(file_path)
                model.removeRow(item.row())
            except OSError as e:
                print(f"Failed to delete {item.text()}: {str(e)}")
        
    @Slot()
    def close_ui_8_and_open_ui_1(self):
        self.ui_1_window = UI_1App()
        self.ui_1_window.show()
        self.close()

    @Slot()
    def close_ui_8_and_open_ui_3(self):
        self.ui_3_window = UI_3App()
        self.ui_3_window.show()
        self.close()
        
    @Slot()
    def close_ui_8_and_open_ui_4(self):
        self.ui_4_window = UI_4App()
        self.ui_4_window.show()
        self.close()
    
    @Slot()
    def close_ui_8_and_open_ui_6(self):
        self.ui_6_window = UI_6App()
        self.ui_6_window.show()
        self.close()

class UI_helpApp(QMainWindow):
    def __init__(self):
        super(UI_helpApp, self).__init__()
        self.ui = Ui_MainWindowhelp()
        self.ui.setupUi(self)
        self.setFixedSize(1040, 600)
        self.ui.pushButton_3.clicked.connect(self.close_ui_help_and_open_ui_2)
    
    @Slot()
    def close_ui_help_and_open_ui_2(self):
        self.ui_2_window = UI_2App()
        self.ui_2_window.show()
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui2_window = UI_2App()
    ui2_window.setFixedSize(1040, 600)
    ui2_window.show()
    sys.exit(app.exec())
