#PyQt Controls

import sys
from Class import Controls
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Controls
    w = Controls()

    sys.exit(app.exec_())