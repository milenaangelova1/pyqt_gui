from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
import sys

from registration import Registration


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("Login GUI")
        self.setGeometry(100, 100, 400, 230)
        self.login_user_interface()
        self.show()

    def login_user_interface(self):
        """
        Create the login GUI
        """
        login_label = QLabel("login", self)
        login_label.move(180, 10)
        login_label.setFont(QFont('Arial', 20))

        name_label = QLabel("username:", self)
        name_label.move(30, 60)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(110, 60)
        self.name_entry.resize(220, 20)

        pass_label = QLabel("password:", self)
        pass_label.move(30, 90)

        self.pass_entry = QLineEdit(self)
        self.pass_entry.move(110, 90)
        self.pass_entry.resize(220, 20)

        sign_in_button = QPushButton('login', self)
        sign_in_button.move(110, 140)
        sign_in_button.resize(200, 40)
        sign_in_button.clicked.connect(self.click_login)

        show_pass_cb = QCheckBox("show password", self)
        show_pass_cb.move(110, 115)
        show_pass_cb.stateChanged.connect(self.show_password)
        show_pass_cb.toggle()
        show_pass_cb.setChecked(False)

        not_a_member = QLabel("not a member?", self)
        not_a_member.move(70, 200)

        sign_up = QPushButton("sign up", self)
        sign_up.move(160, 195)
        sign_up.clicked.connect(self.create_new_user)

    def click_login(self):
        """
        When user clicks sign in button, check username and password
        match any existing profiles in users.txt.
        If they exists, display error messagebox.
        """
        users = {} # create empty dictionary to store user information
        # Check id users.txt exists, otherwise create new file
        try:
            with open("files/users.txt", "r") as f:
                for line in f:
                    user_fields = line.split(" ")
                    username = user_fields[0]
                    password = user_fields[1].strip('\n')
                    users[username] = password
        except FileNotFoundError:
            print("The file does not exists. Creating a new file.")
            open("files/users.txt", "w")

        username = self.name_entry.text()
        password = self.pass_entry.text()

        if (username, password) in users.items():
            QMessageBox.information(self, "Login Successful!", "Login Successful!",
                                    QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error Message", "The username or password is incorrect.",
                                QMessageBox.Cancel, QMessageBox.Cancel)

    def show_password(self, state):
        """
        If checkbox is enabled, view password.
        Else, mask password so others cannot see it.
        :param state: state of the checkbox - True or False
        """
        if state == Qt.Checked:
            self.pass_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.pass_entry.setEchoMode(QLineEdit.Password)

    def create_new_user(self):
        """
        When the sign up button is clicked, open a new window and allow
        the user to create a new account.
        """
        self.create_new_user_dialog = Registration()
        self.create_new_user_dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec_())
