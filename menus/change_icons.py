import sys, random

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout


class ChangeIcons(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('Set Icons Example')
        self.setWindowIcon(QIcon('images/pyqt_logo.png'))
        self.create_widgets()
        self.show()

    def create_widgets(self):
        """
        Set up widgets.
        """
        info_label = QLabel("Click on the button and select a fruit")

        self.images = [
            "images/1_apple.png", "images/2_pineapple.png",
            "images/3_watermelon.png", "images/4_banana.png"
        ]
        self.icon_button = QPushButton(self)
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.change_button_icon)

        # create vertical layout and add widgets
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)

        # set main layout of window
        self.setLayout(v_box)

    def change_button_icon(self):
        """
        When the button is clicked, change the icon to one of the
        images in the list.
        """
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChangeIcons()
    sys.exit(app.exec_())
