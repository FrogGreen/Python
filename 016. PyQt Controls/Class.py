from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPlainTextEdit, QListWidget, QScrollArea, QKeySequenceEdit, QPushButton, QRadioButton, QCheckBox, QComboBox, QDialogButtonBox, QDoubleSpinBox, QGridLayout, QFormLayout, QGroupBox, QApplication

class Controls(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        entries = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        self.centralwidget = QWidget(self)
        grid = QGridLayout()

        #Label
        grid.addWidget(QLabel("Label"), 0, 0)

        #QLineEdit
        grid.addWidget(QLineEdit("QLineEdit"), 0, 1)

        #QPlainTextEdit
        grid.addWidget(QPlainTextEdit("QPlainTextEdit"), 0, 2)

        #QListWidget
        listWidget = QListWidget()
        listWidget.addItems(entries)
        grid.addWidget(listWidget, 0, 3)

        #QScrollArea
        scrollArea = QScrollArea()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel(entries[0]))
        formLayout.addRow(QLabel(entries[1]))
        formLayout.addRow(QLabel(entries[2]))
        formLayout.addRow(QLabel(entries[3]))
        formLayout.addRow(QLabel(entries[4]))
        formLayout.addRow(QLabel(entries[5]))
        formLayout.addRow(QLabel(entries[6]))
        #QGroupBox
        groupBox = QGroupBox("This Is Group Box")
        groupBox.setLayout(formLayout)
        scrollArea.setWidget(groupBox)
        scrollArea.setWidgetResizable(True)
        grid.addWidget(scrollArea, 0, 4)

        #QKeySequenceEdit
        grid.addWidget(QKeySequenceEdit("QKeySequenceEdit"), 0, 5)

        #QPushButton
        grid.addWidget(QPushButton("QPushButton"), 1, 0)

        #QRadioButton
        grid.addWidget(QRadioButton("QRadioButton"), 1, 1)

        #QCheckBox
        grid.addWidget(QCheckBox("QCheckBox"), 1, 2)

        #QComboBox
        comboBox = QComboBox()
        comboBox.addItems(entries)
        grid.addWidget(comboBox, 1, 3)

        #QDialogButtonBox
        grid.addWidget(QDialogButtonBox(QDialogButtonBox.Cancel|QDialogButtonBox.Ok), 1, 4)

        #QDoubleSpinBox
        grid.addWidget(QDoubleSpinBox(), 1, 5)

        self.setLayout(grid)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Controls")
        self.show()