import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QLineEdit, QMessageBox, QPushButton


class DialogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """
            Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QMessageBox Example')
        self.display_widgets()  # call out display widgets
        self.show()

    def display_widgets(self):
        """
        Setup the widgets.
        """
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(20, 20)
        catalogue_label.setFont(QFont('Arial', 20))

        auth_label = QLabel("Enter the name of the author you are searching for:", self)
        auth_label.move(40, 60)
        author_name = QLabel("Name:", self)
        author_name.move(50, 90)

        self.auth_entry = QLineEdit(self)
        self.auth_entry.move(95, 90)
        self.auth_entry.resize(240, 20)
        self.auth_entry.setPlaceholderText("firstname lastname")

        search_button = QPushButton("Search", self)
        search_button.move(125, 130)
        search_button.resize(150, 40)
        search_button.clicked.connect(self.display_message_box)

    def display_message_box(self):
        """
        When button is clicked, search through catalogue of names.
        if name is found, display Author Found dialog.
        Otherwise, display Author Not Found dialog.
        """
        try:
            with open("files/authors.txt", "r") as f:
                authors = [line.rstrip("\n") for line in f]
        except FileNotFoundError:
            print("The file cannot be found.")

        # Check for name in list
        if self.auth_entry.text() in authors:
            QMessageBox().information(self, "Author Found", "Author Found in the catalogue!",
                                      QMessageBox.Ok, QMessageBox.Ok)
        else:
            not_found_msg = QMessageBox.question(self, "Author Not Found",
                                                 "Author not found in catalogue."
                                                 "Do you wish to continue?",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if not_found_msg == QMessageBox.No:
                print("Closing application.")
                self.close()
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DialogWindow()
    sys.exit(app.exec_())
