#PyQt Layouts

import sys
from Class import Positions, Boxes, Grids
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Layout - Positions
    w = Positions()

    #Layout - Boxes
    #w = Boxes()

    #Layout - Boxes
    #w = Grids()

    sys.exit(app.exec_())