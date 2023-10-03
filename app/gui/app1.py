import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from PySide6.QtCore import QDir, Qt, QStateMachine, QState, Signal
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

        self.show_file_list()

        # 상태 머신을 설정합니다.
        self.state_machine = QStateMachine(self)

        # UI_1에서 UI_2로 전환하는 상태를 정의합니다.
        self.state_ui1_to_ui2 = QState()
        self.state_ui1_to_ui2.assignProperty(self, "windowTitle", "UI_2")
        self.ui.pushButton_3.clicked.connect(self.state_ui1_to_ui2.trigger)
        self.state_ui1_to_ui2.addTransition(self.state_ui1_to_ui2, Signal("entered()"), self.show_ui2)

        # 상태 머신에 상태를 추가합니다.
        self.state_machine.addState(self.state_ui1_to_ui2)
        self.state_machine.setInitialState(self.state_ui1_to_ui2)
        self.state_machine.start()

    def show_file_list(self):
        current_directory = QDir.currentPath()
        file_list = os.listdir(current_directory)
        file_list = [item for item in file_list if os.path.isdir(item) or os.path.isfile(item)]

        model = QStandardItemModel()
        for item_text in file_list:
            item = CheckableItem(item_text)
            model.appendRow(item)

        self.ui.listView.setModel(model)

    def show_ui2(self):
        self.ui_2.show()
        self.hide()

class UI_2App(QMainWindow):
    def __init__(self):
        super(UI_2App, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

        # 상태 머신을 설정합니다.
        self.state_ui2_to_ui1 = QState()
        self.state_ui2_to_ui1.assignProperty(self, "windowTitle", "UI_1")
        self.ui.pushButton_4.clicked.connect(self.state_ui2_to_ui1.trigger)
        self.state_ui2_to_ui1.addTransition(self.state_ui2_to_ui1, Signal("entered()"), self.show_ui1)

        self.state_machine = QStateMachine(self)
        self.state_machine.addState(self.state_ui2_to_ui1)
        self.state_machine.setInitialState(self.state_ui2_to_ui1)
        self.state_machine.start()

    def show_ui1(self):
        self.ui_1.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = UI_1App()
    window.ui_1 = window
    window.ui_2 = UI_2App()

    window.show_ui1()
    window.show()

    sys.exit(app.exec_())
