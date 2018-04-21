from PyQt5 import QtCore, QtGui, QtWidgets
import Dijkstra_view
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(320, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 40, 161, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 80, 161, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 231, 23))
        self.pushButton.setMinimumSize(QtCore.QSize(231, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(231, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setAlgoritgm)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Пошук найкоротшого шляху"))
        self.radioButton.setText(_translate("MainWindow", "Алгоритм А зірка"))
        self.radioButton_2.setText(_translate("MainWindow", "Алгоритм Дейкстри"))
        self.pushButton.setText(_translate("MainWindow", "Перейти до виконання"))

    def setAlgoritgm(self):
        if self.radioButton.isChecked():
            pass
        elif self.radioButton_2.isChecked():
            widget = QtWidgets.QDialog()
            View = Dijkstra_view.Ui_Dialog()
            View.setupUi(widget)
            widget.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    game = Ui_MainWindow()
    game.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
