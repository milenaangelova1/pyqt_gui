import sys, csv
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QVBoxLayout


class ModelView(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle('Model and View example')

        self.setupModelView()
        self.show()

    def setupModelView(self):
        self.model = QStandardItemModel()
        table_view = QTableView()
        table_view.setModel(self.model)

        self.model.setRowCount(3)
        self.model.setColumnCount(4)

        self.loadCSVFile()

        v_box = QVBoxLayout()
        v_box.addWidget(table_view)
        self.setLayout(v_box)

    def loadCSVFile(self):
        """
        Load header and rows from CSV file.
        """
        file_name = "files/parts.csv"

        try:
            with open(file_name, "r") as csv_f:
                reader = csv.reader(csv_f)
                header_labels = next(reader)
                self.model.setHorizontalHeaderLabels(header_labels)
                for i, row in enumerate(csv.reader(csv_f)):
                    items = [QStandardItem(item) for item in row]
                    self.model.insertRow(i, items)
        except FileNotFoundError:
            print("The file doesn't exist.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ModelView()
    sys.exit(app.exec_())

