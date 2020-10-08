import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QLabel, QHBoxLayout, QButtonGroup, QVBoxLayout, \
    QRadioButton, QGroupBox, QPushButton


class FoodOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setMinimumSize(600, 700)
        self.setWindowTitle('Food Order GUI')
        self.setupTabsAndLayout()
        self.show()

    def setupTabsAndLayout(self):
        """
        Set up tab bar and different tab widgets.
        Also, create the side widget to display items selected.
        """
        self.tab_bar = QTabWidget()

        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tabs")

        self.wings_tab = QWidget()
        self.wings_tab.setObjectName("Tabs")

        self.tab_bar.addTab(self.pizza_tab, "Pizza")
        self.tab_bar.addTab(self.wings_tab, "Wings")

        self.pizzaTab()
        self.wingsTab()

    def pizzaTab(self):
        """
        Create the pizza tab. Allows the user to select the type
        of pizza and topping using radio buttons.
        """
        tab_pizza_label = QLabel("BUILD YOUR OWN PIZZA")
        tab_pizza_label.setObjectName("Header")

        description_box = QWidget()
        description_box.setObjectName("ImageBorder")

        pizza_image_path = "images/pizza.png"
        pizza_image = self.loadImage(pizza_image_path)

        pizza_desc = QLabel()
        pizza_desc.setObjectName("ImageInfo")

        pizza_desc.setText("Build a custom pizza for you. Start with your favorite crust and add any toppings, plus the perfect amount of cheese and sauce.")
        pizza_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(pizza_image)
        h_box.addWidget(pizza_desc)

        description_box.setLayout(h_box)

        crust_gbox = QGroupBox()
        crust_gbox.setTitle("CHOOSE YOUR CRUST")

        self.crust_group = QButtonGroup()
        gb_v_box = QVBoxLayout()
        crust_list = ["Hand-Tossed", "Flat", "Stuffed"]

        for cr in crust_list:
            crust_rb = QRadioButton(cr)
            gb_v_box.addWidget(crust_rb)
            self.crust_group.addButton(crust_rb)

        crust_gbox.setLayout(gb_v_box)

        # Create group box that will contain toppings choices
        toppings_gbox = QGroupBox()
        toppings_gbox.setTitle("CHOOSE YOUR TOPPINGS")

        # Set up button group for toppings radio buttons
        self.toppings_group = QButtonGroup()
        gb_v_box = QVBoxLayout()

        toppings_list = ["Pepperoni", "Sausage", "Bacon", "Canadian Bacon",
                         "Beef", "Pineapple", "Mushroom", "Onion",
                         "Olive", "Green Pepper", "Tomato", "Spinach", "Cheese"]
        # Create radio buttons for the different toppings and
        # add to layout
        for top in toppings_list:
            toppings_rb = QRadioButton(top)
            gb_v_box.addWidget(toppings_rb)
            self.toppings_group.addButton(toppings_rb)
        self.toppings_group.setExclusive(False)

        toppings_gbox.setLayout(gb_v_box)

        # Create button to add information to side widget
        # when clicked
        add_to_order_button1 = QPushButton("Add To Order")
        add_to_order_button1.clicked.connect(self.displayPizzaInOrder)

        # create layout for pizza tab (page 1)
        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_pizza_label)
        page1_v_box.addWidget(description_box)
        page1_v_box.addWidget(crust_gbox)
        page1_v_box.addWidget(toppings_gbox)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_to_order_button1, alignment=Qt.AlignRight)

        self.pizza_tab.setLayout(page1_v_box)

    def wingsTab(self):
        pass

    def displayPizzaInOrder(self):
        pass

    def loadImage(self, path):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FoodOrder()
    sys.exit(app.exec_())

