import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QSpinBox, QComboBox, QTextEdit, QPushButton, \
    QFormLayout, QHBoxLayout


class ApplicationFormWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Application Form GUI')
        self.form_widgets()
        self.show()

    def form_widgets(self):
        """
        Create widgets that will be used in the application form
        """
        # Create widgets
        title = QLabel("Appointment Submission Form")
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)

        name = QLineEdit()
        name.resize(100, 100)
        address = QLineEdit()

        mobile_num = QLineEdit()
        mobile_num.setInputMask("000-000-0000;")

        age_label = QLabel("Age")
        age = QSpinBox()
        age.setRange(1, 110)

        height_label = QLabel("Height")
        height = QLineEdit()
        height.setPlaceholderText("cm")

        weight_label = QLabel("Weight")
        weight = QLineEdit()
        weight.setPlaceholderText("kg")

        gender = QComboBox()
        gender.addItems(["Male", "Female"])

        surgery = QTextEdit()
        surgery.setPlaceholderText("separate by ','")

        blood_type = QComboBox()
        blood_type.addItems(["A", "B", "AB", "O"])

        hours = QSpinBox()
        hours.setRange(1, 12)

        minutes = QComboBox()
        minutes.addItems([":00", ":15", ":30", ":45"])

        am_pm = QComboBox()
        am_pm.addItems(["AM", "PM"])

        submit_button = QPushButton("Submit Appointment")
        submit_button.clicked.connect(self.close)

        h_box = QHBoxLayout()
        h_box.addSpacing(10)
        h_box.addWidget(age_label)
        h_box.addWidget(age)
        h_box.addWidget(height_label)
        h_box.addWidget(height)
        h_box.addWidget(weight_label)
        h_box.addWidget(weight)

        desired_time_h_box = QHBoxLayout()
        desired_time_h_box.addSpacing(10)
        desired_time_h_box.addWidget(hours)
        desired_time_h_box.addWidget(minutes)
        desired_time_h_box.addWidget(am_pm)

        app_form_layout = QFormLayout()
        app_form_layout.addRow(title)
        app_form_layout.addRow("Address", address)
        app_form_layout.addRow("Mobile Number", mobile_num)
        app_form_layout.addRow(h_box)
        app_form_layout.addRow("Gender", gender)
        app_form_layout.addRow("Past Surgeries ", surgery)
        app_form_layout.addRow("Blood Type", blood_type)
        app_form_layout.addRow("Desired Time", desired_time_h_box)
        app_form_layout.addRow(submit_button)

        self.setLayout(app_form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ApplicationFormWindow()
    sys.exit(app.exec_())
