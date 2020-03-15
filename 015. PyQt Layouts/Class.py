from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QApplication

class Positions(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        labelOne = QLabel("Label One", self)
        labelOne.move(15, 10)
        labelTwo = QLabel("Label Two", self)
        labelTwo.move(45, 40)
        LabelThree = QLabel("Label Three", self)
        LabelThree.move(75, 70)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Layout - Positions")
        self.show()


class Boxes(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        labelOne = QLabel("Label One")
        labelTwo = QLabel("Label Two")
        labelThree = QPushButton("Label Three")
        hbox = QHBoxLayout()
        hbox.addWidget(labelOne)
        hbox.addStretch(5)
        hbox.addWidget(labelTwo)
        hbox.addStretch(10)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(5)
        vbox.addWidget(labelThree)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Layout - Boxes")
        self.show()


class Grids(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ["", "01", "02", "03",
                 "04", "05", "06", "07",
                "08", "09", "10", "11",
                 "12", "13", "14", "15",
                "16", "17", "18", "19"]
        positions = [(i,j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == "":
                continue
            label = QLabel(name)
            grid.addWidget(label, *position)
        grid.addWidget(QLabel("20"), 5, 1)
        self.move(300, 150)
        self.setWindowTitle("Layout - Grids")
        self.show()