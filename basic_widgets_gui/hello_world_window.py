import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabel Example')
        self.display_labels()
        self.show()

    def display_labels(self):
        """
        Display text and images using QLabels.
        Check to see if image file exists, if not throw an exception.
        """
        text = QLabel(self)
        text.setText("Hello")
        text.move(105, 15)

        image = "images/world.png"
        try:
            with open(image):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25, 40)
        except FileNotFoundError:
            print("Image not Found.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())
