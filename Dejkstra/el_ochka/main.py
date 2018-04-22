from PyQt5 import QtCore, QtGui, QtWidgets, uic
from el_lang.lang import Lang
import sys
from el_core.UI import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Ui_MainWindow()
    widget.show()
    sys.exit(app.exec_())
