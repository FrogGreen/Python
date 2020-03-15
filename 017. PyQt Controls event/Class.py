from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFormLayout, QApplication

class ControlsEvent(QWidget):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.text = "You've pushed button {0} times".format(self.x)
        self.initUI()

    def initUI(self):
        #QLabel
        self.label = QLabel(self.text)

        #QPushButton
        pushButton = QPushButton("Push me")

        #FormLayout
        formLayout = QFormLayout()
        formLayout.addRow(self.label, pushButton)
        self.setLayout(formLayout)

        #PushButton Event
        pushButton.clicked.connect(self.buttonClicked)

        self.move(300, 300)
        self.setWindowTitle("Controls event")
        self.show()

    def buttonClicked(self):
        print("button pressed")
        self.x = self.x + 1
        self.text = "You've pushed button {0} times".format(self.x)
        self.label.setText(self.text)