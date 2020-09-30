import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QCheckBox


class CheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """
            Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QCheckBox Widget')
        self.display_checkboxes()
        self.show()

    def display_checkboxes(self):
        """
        Setup the checkboxes and other widgets
        """
        header_label = QLabel(self)
        header_label.setText("Which shifts can you work? "
                             "(Please check all that apply)")
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        morning_cb = QCheckBox("Morning [8 AM-2 PM]", self)
        morning_cb.move(20, 80)
        morning_cb.stateChanged.connect(self.print_to_terminal)

        after_cb = QCheckBox("Afternoon [1 PM-8 PM]", self)
        after_cb.move(20, 100)
        after_cb.stateChanged.connect(self.print_to_terminal)

        night_cb = QCheckBox("Night [7 PM-3 AM]", self)
        night_cb.move(20, 120)
        night_cb.stateChanged.connect(self.print_to_terminal)

    def print_to_terminal(self, state):
        """
        Simple function to show how to determine the state of a checkbox.
        Prints the text label of the checkbox by determining which widget is
        sending the signal.
        :param state:
        """
        sender = self.sender()
        if state:
            print("{} Selected.".format(sender.text()))
        else:
            print("{} Deselected.".format(sender.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())
