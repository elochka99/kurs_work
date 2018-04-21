from PyQt5 import QtCore, QtGui, QtWidgets
from Dijkstra import Dijkstra
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dijkstra_n = None
        self.Dijkstra_m = None
        self.Dijkstra_start = None
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        #self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        #self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        #self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.l_number = QtWidgets.QLabel(self.tab)
        self.l_number.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.l_number.setObjectName("l_number")
        self.i_number = QtWidgets.QLineEdit(self.tab)
        self.i_number.setGeometry(QtCore.QRect(20, 40, 140, 20))
        self.i_number.setObjectName("i_number")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(250, 70, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.connectors_table = QtWidgets.QTableWidget(self.tab)
        self.connectors_table.setGeometry(QtCore.QRect(190, 120, 256, 192))
        self.connectors_table.setObjectName("connectors_table")
        self.connectors_table.setColumnCount(0)
        self.connectors_table.setRowCount(0)
        self.generate = QtWidgets.QPushButton(self.tab)
        self.generate.setGeometry(QtCore.QRect(250, 332, 141, 23))
        self.generate.setObjectName("generate")
        self.i_m_number = QtWidgets.QLineEdit(self.tab)
        self.i_m_number.setGeometry(QtCore.QRect(250, 40, 140, 20))
        self.i_m_number.setObjectName("i_m_number")
        self.l_m_number = QtWidgets.QLabel(self.tab)
        self.l_m_number.setGeometry(QtCore.QRect(250, 20, 111, 16))
        self.l_m_number.setObjectName("l_m_number")
        self.i_start = QtWidgets.QLineEdit(self.tab)
        self.i_start.setGeometry(QtCore.QRect(470, 40, 140, 20))
        self.i_start.setObjectName("i_start")
        self.l_start = QtWidgets.QLabel(self.tab)
        self.l_start.setGeometry(QtCore.QRect(470, 20, 111, 16))
        self.l_start.setObjectName("l_start")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 0, 621, 401))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_2, "")
        
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.connectors_table.cellChanged.connect(self._handleCellChanged)
        Dialog.setWindowTitle(_translate("Dialog", "Дейкстра"))
        self.l_number.setText(_translate("Dialog", "Кількість точок:"))
        self.pushButton.setText(_translate("Dialog", "Генерувати"))
        self.generate.setText(_translate("Dialog", "Виконати"))
        self.l_m_number.setText(_translate("Dialog", "Кількість Ребр:"))
        self.l_start.setText(_translate("Dialog", "Початкова точка:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Головна"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Результат роботи"))
        self.pushButton.clicked.connect(self.create_table)
        self.generate.clicked.connect(self._handleGenerate)

    def _handleCellChanged(self, row, column):
        try:
            int(self.connectors_table.item(row, column).text())
        except ValueError:
            self.connectors_table.item(row, column).setText("0")
        #print(row, column, self.connectors_table.item(row, column).text())

    def create_table(self):
        try:
            self.Dijkstra_n = int(self.i_number.text())
            self.Dijkstra_m = int(self.i_m_number.text())
            self.Dijkstra_start = int(self.i_start.text())
        except ValueError:
            self.Dijkstra_n = None
            self.Dijkstra_m = None
            self.Dijkstra_start = None

        if type(self.Dijkstra_n) is int and type(self.Dijkstra_m) is int and type(self.Dijkstra_start) is int:
            self.connectors_table.setColumnCount(3)
            self.connectors_table.setRowCount(self.Dijkstra_m)
            self.connectors_table.setHorizontalHeaderLabels(["Точка 1", "Точка 2", "Сумма ребра"])
            self.connectors_table.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignLeft)
            self.connectors_table.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.connectors_table.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignRight)
            self.connectors_table.resizeColumnsToContents()

    def _handleGenerate(self):
        dijkstra = Dijkstra()
        if type(self.Dijkstra_n) is int and type(self.Dijkstra_m) is int and type(self.Dijkstra_start) is int:
            count = 0
            data = []
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText("Зєднання: ")
            self.plainTextEdit.appendPlainText("Точка 1\tТочка 2\tСумма зєднання")
            for row in range(0, self.connectors_table.rowCount()):
                temp = []
                for column in range(0, self.connectors_table.columnCount()):
                    if self.connectors_table.item(row, column) is None:
                        count += 1
                    else:
                        temp.append(int(self.connectors_table.item(row, column).text()))
                self.plainTextEdit.appendPlainText(' \t'.join(str(i) for i in temp))
                data.append(temp)
            if count == 0:
                dijkstra.readdata(self.Dijkstra_n, self.Dijkstra_m, self.Dijkstra_start, data)
                temp = dijkstra.printdata()
                self.plainTextEdit.appendPlainText("Данні проходження: ")
                self.plainTextEdit.appendPlainText(', '.join(str(i) for i in temp['bytes']))
                self.plainTextEdit.appendPlainText("Найкоротші шляхи для проходження: ")
                for i in range(len(temp['path'])):
                    to_return = ' -> '.join(str(x) for x in temp['path'][i + 1])
                    self.plainTextEdit.appendPlainText(str(i + 1) + ": " + to_return)
                    
                self.tabWidget.setCurrentIndex(1)                
