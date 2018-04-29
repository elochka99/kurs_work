from PyQt5 import QtCore, QtGui, QtWidgets, uic
from el_lang.lang import Lang
import sys
from el_core.UI import Ui_MainWindow

sys._excepthook = sys.excepthook
def my_exception_hook(exctype, value, traceback):
    """
    method called if program raised and send the data
    ro the console
    """
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = my_exception_hook

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Ui_MainWindow()
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        pass
