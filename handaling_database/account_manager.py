import sys, os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLabel, QSizePolicy, QPushButton, QComboBox, \
    QHBoxLayout, QTableView, QHeaderView, QVBoxLayout


class AccountManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setMinimumSize(1000, 600)
        self.setWindowTitle('Account Manager GUI')

        self.createConnection()
        self.createTable()
        self.setupWidgets()
        self.show()

    def createConnection(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1)  # Error code 1 - signifies error

        # Check if tables we need exist in the database
        tables_needed = {'accounts', 'countries'}
        tables_not_found = tables_needed - set(database.tables())

        if tables_not_found:
            QMessageBox.critical(None, "Error", f"The following tables are missing from the database: {tables_not_found}")
            sys.exit(1)

    def createTable(self):
        """
        Set up the model, headers and populate the model.
        """
        self.model = QSqlRelationalTableModel()
        self.model.setTable('accounts')
        self.model.setRelation(self.model.fieldIndex('country_id'), QSqlRelation('countries', 'id', 'country'))

        self.model.setHeaderData(self.model.fieldIndex('id'), Qt.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex('employee_id'), Qt.Horizontal, "Employee ID")
        self.model.setHeaderData(self.model.fieldIndex('first_name'), Qt.Horizontal, "First")
        self.model.setHeaderData(self.model.fieldIndex('last_name'), Qt.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex('email'), Qt.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex('department'), Qt.Horizontal, "Dept.")
        self.model.setHeaderData(self.model.fieldIndex('country_id'), Qt.Horizontal, "Country")

        # populate the model with data
        self.model.select()

    def setupWidgets(self):
        """
        Create instances of widgets, the table view and set layouts.
        """
        icons_path = "icons"

        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("font: bold 24px")

        add_product_button = QPushButton("Add Employee")
        add_product_button.setIcon(QIcon(os.path.join(icons_path, "add_user.png")))
        add_product_button.setStyleSheet("padding: 10px")
        add_product_button.clicked.connect(self.addItem)

        del_product_button = QPushButton("Delete")
        del_product_button.setIcon(QIcon(os.path.join(icons_path, "trash_can.png")))
        del_product_button.setStyleSheet("padding: 10px")
        del_product_button.clicked.connect(self.deleteItem)

        # set up sorting combobox
        sorting_options = ["Sort by ID", "Sort by Employee ID", "Sort by First Name",
                           "Sort by Last Name", "Sort by Department", "Sort by Country"]

        sort_name_cb = QComboBox()
        sort_name_cb.addItems(sorting_options)
        sort_name_cb.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_product_button)
        buttons_h_box.addWidget(del_product_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_name_cb)

        # Widget to contain editing buttons
        edit_buttons = QWidget()
        edit_buttons.setLayout(buttons_h_box)

        # Create table view and set model
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)

        # Instantiate the delegate
        delegate = QSqlRelationalDelegate(self.table_view)
        self.table_view.setItemDelegate(delegate)

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignLeft)
        main_v_box.addWidget(edit_buttons)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addItem(self):
        pass

    def deleteItem(self):
        pass

    def setSortingOrder(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AccountManager()
    sys.exit(app.exec_())

