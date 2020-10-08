import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt')
        self.create_qlabel()
        self.show()

    def create_qlabel(self):
        label = QLabel("Test", self)
        label.setStyleSheet("""
            background-color: skyblue;
            color: white;
            border-style: outset;
            border-radius: 5px;
            border-width: 3px;
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())

