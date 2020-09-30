import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class ButtonWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """
            Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('QPushButton Widget')
        self.display_button()  # call out display button function
        self.show()

    def display_button(self):
        """
        Setup the button widget.
        """
        name_label = QLabel(self)
        name_label.setText("Don't push the button.")
        name_label.move(60, 30)  # arrange label

        button = QPushButton("Push Me", self)
        button.clicked.connect(self.button_clicked)
        button.move(80, 70)

    def button_clicked(self):
        """
        Print message to terminal, and close the window when button is clicked.
        """
        print("The window has been closed.")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonWindow()
    sys.exit(app.exec_())
