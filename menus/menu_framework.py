from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys


class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example')
        self.create_menu()

        self.show()

    def create_menu(self):
        """
        Create skeleton for file menu
        """
        exit_act = QAction("&Exit", self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        # create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())
