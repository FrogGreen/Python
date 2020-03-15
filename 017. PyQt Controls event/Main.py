#PyQt Controls event

import sys
from Class import ControlsEvent
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Controls event
    w = ControlsEvent()

    sys.exit(app.exec_())