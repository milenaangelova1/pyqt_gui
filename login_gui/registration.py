from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox
import sys


class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Create new account')
        self.display_widgets_to_collect_info()
        self.show()

    def display_widgets_to_collect_info(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account.
        """
        new_user_image = "images/new_user_icon.png"
        try:
            with open(new_user_image):
                new_user = QLabel(self)
                pixmap = QPixmap(new_user_image)
                new_user.setPixmap(pixmap)
                new_user.move(150, 60)
        except FileNotFoundError:
            print("Image not found.")

        # widget_labels = [
        #     ("create new account", 110, 20, 'Arial', 20),
        #     ("username:", 50, 180, 'Arial', 17),
        #     ("full name", 50, 240, 'Arial', 17)
        # ]

        sign_up_label = QLabel("create new account", self)
        sign_up_label.move(110, 20)
        sign_up_label.setFont(QFont('Arial', 20))

        name_label = QLabel("username:", self)
        name_label.move(50, 180)

        full_name_label = QLabel("full name:", self)
        full_name_label.move(50, 210)

        pass_label = QLabel("password:", self)
        pass_label.move(50, 240)

        confirm_label = QLabel("confirm:", self)
        confirm_label.move(50, 270)

        # text fields - QLineEdit
        # username
        self.name_entry = QLineEdit(self)
        self.name_entry.move(130, 180)
        self.name_entry.resize(200, 20)

        # full name
        name_entry = QLineEdit(self)
        name_entry.move(130, 210)
        name_entry.resize(200, 20)

        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.pswd_entry.move(130, 240)
        self.pswd_entry.resize(200, 20)

        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.move(130, 270)
        self.confirm_entry.resize(200, 20)

        # create a sign up button
        sign_up_button = QPushButton("sign up", self)
        sign_up_button.move(100, 310)
        sign_up_button.resize(200, 40)
        sign_up_button.clicked.connect(self.confirm_sign_up)

    def confirm_sign_up(self):
        """
        When user presses sign up, check if the password match.
        If the match, then save username and password text to users.txt
        """
        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()

        if pswd_text != confirm_text:
            # Display messageBox id passwords don't match
            QMessageBox.warning(self, "Error Message", "The passwords you entered do not match."
                                "Please try again", QMessageBox.Close, QMessageBox.Close)
        else:
            with open("files/users.txt", "a+") as f:
                f.write(self.name_entry.text() + " ")
                f.write(pswd_text + "\n")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Registration()
    sys.exit(app.exec_())
