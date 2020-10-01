import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QMessageBox, QFileDialog


class NotepadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Notepad GUI')
        self.notepad_widgets()
        self.show()

    def notepad_widgets(self):
        """
        Clear widgets for notepadGUI and arrange them in window
        """
        # Create push buttons for editing menu
        new_button = QPushButton("New", self)
        new_button.move(10, 20)
        new_button.clicked.connect(self.clear_text)

        save_button = QPushButton("Save", self)
        save_button.move(80, 20)
        save_button.clicked.connect(self.save_text)

        self.text_field = QTextEdit(self)
        self.text_field.move(10, 60)
        self.text_field.resize(280, 330)

    def clear_text(self):
        """
        If the new button is clicked, display dialog asking user of they want to clear the text
        edit field or not.
        """
        answer = QMessageBox.question(self, "Clear Text", "Do you want to clear the text?",
                                      QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            self.text_field.clear()
        else:
            pass

    def save_text(self):
        options = QFileDialog.Options()
        notepad_text = self.text_field.toPlainText()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '','All Files (*);;Text Files(*.txt)', options=options)
        if file_name:
            with open(file_name, "w") as f:
                f.write(notepad_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotepadWindow()
    sys.exit(app.exec_())
