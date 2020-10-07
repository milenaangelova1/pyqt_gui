from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QToolBar, QDockWidget, QStatusBar
import sys


class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Basic Menu Example')
        self.setCentralWidget(QTextEdit())
        self.create_menu()
        self.create_toolbar()
        self.create_dock_widget()

        self.show()

    def create_menu(self):
        """
        Create skeleton for file menu
        """
        self.exit_act = QAction(QIcon('images/exit.png'), "&Exit", self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        full_screen_act = QAction('Full Screen', self, checkable=True)
        full_screen_act.setStatusTip('Switch to full screen mode')
        full_screen_act.triggered.connect(self.switch_to_full_screen)

        # create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)

        # Create view menu, Appearance submenu and add actions
        view_menu = menu_bar.addMenu('View')
        appearance_submenu = view_menu.addMenu('Appearance')
        appearance_submenu.addAction(full_screen_act)

        # Display info about tools, menu, and view in statusbar
        self.setStatusBar(QStatusBar(self))

    def create_toolbar(self):
        """
        Create toolbar for GUI
        """
        # set up toolbar
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)
        tool_bar.addAction(self.exit_act)

    def create_dock_widget(self):
        """
        Create dock widget
        """
        # set up dock widget
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.RightDockWidgetArea)

        # set main widget for the dock widget
        dock_widget.setWidget(QTextEdit())

        # set initial location of dock widget in main window
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def switch_to_full_screen(self, state):
        """
        If state is True, then display the main window in full screen.
        Otherwise, return the window to normal
        :param state: boolean
        """
        if state:
            self.showFullScreen()
        else:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())
