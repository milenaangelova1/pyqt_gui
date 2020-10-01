import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QButtonGroup, QCheckBox, \
    QPushButton


class SurveyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Survey GUI')
        self.display_widgets()
        self.show()

    def display_widgets(self):
        """
        Set up widgets using QHBoxLayout and QVBoxLayout
        """
        # Create label and button widgets
        title = QLabel("Restaurant Name")
        title.setFont(QFont('Arial', 17))

        question = QLabel("How would you rate your service today?")

        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()

        ratings = ["Not Satisfied", "Average", "Satisfied"]
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(60)
        ratings_h_box.addStretch()

        for rating in ratings:
            rate_label = QLabel(rating, self)
            ratings_h_box.addWidget(rate_label)
            ratings_h_box.addStretch()

        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100)
        scale_bg = QButtonGroup(self)
        cb_h_box.addStretch()

        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb), self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()
        scale_bg.buttonClicked.connect(self.checkbox_clicked)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        # Create vertical layout and add widgets and h_box layouts
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_button)

        # set main layout of the window
        self.setLayout(v_box)

    def checkbox_clicked(self, cb):
        """
        Print the text of checkbox selected.
        :param cb: checkbox
        """
        print("{} Selected".format(cb.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SurveyWindow()
    sys.exit(app.exec_())
