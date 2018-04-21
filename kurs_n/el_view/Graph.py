# -*- coding: utf-8 -*-

"""
Graph.py - Graph GUI Window
Copyright 2018 Olena Horokhova
Distributed under GNU GPL v2 license. See license.txt for more infomation.

This software is provided 'as-is', 
without any express or implied warranty. 
In no event will the authors be held liable 
for any damages arising from the use of this software.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_EnterMatrix(object):
    def setupUi(self, EnterMatrix):
        EnterMatrix.setObjectName("EnterMatrix")
        EnterMatrix.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EnterMatrix.sizePolicy().hasHeightForWidth())
        EnterMatrix.setSizePolicy(sizePolicy)
        EnterMatrix.setMinimumSize(QtCore.QSize(640, 480))
        EnterMatrix.setMaximumSize(QtCore.QSize(640, 480))
        self.buttonBox = QtWidgets.QDialogButtonBox(EnterMatrix)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(EnterMatrix)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 641, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.matrix_main = QtWidgets.QWidget()
        self.matrix_main.setObjectName("matrix_main")
        self.matrix = QtWidgets.QTableWidget(self.matrix_main)
        self.matrix.setGeometry(QtCore.QRect(20, 30, 261, 192))
        self.matrix.setObjectName("matrix")
        self.matrix.setColumnCount(0)
        self.matrix.setRowCount(0)
        self.newmatrix = QtWidgets.QTableWidget(self.matrix_main)
        self.newmatrix.setGeometry(QtCore.QRect(350, 30, 261, 192))
        self.newmatrix.setObjectName("newmatrix")
        self.newmatrix.setColumnCount(0)
        self.newmatrix.setRowCount(0)
        self.generate = QtWidgets.QPushButton(self.matrix_main)
        self.generate.setGeometry(QtCore.QRect(20, 240, 261, 23))
        self.generate.setObjectName("generate")
        self.graph = QtWidgets.QPushButton(self.matrix_main)
        self.graph.setGeometry(QtCore.QRect(350, 240, 261, 23))
        self.graph.setObjectName("graph")
        self.label = QtWidgets.QLabel(self.matrix_main)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.matrix_main)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 261, 16))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.matrix_main, "")
        self.matrix_graph = QtWidgets.QWidget()
        self.matrix_graph.setObjectName("matrix_graph")
        self.log_algorithm = QtWidgets.QTextBrowser(self.matrix_graph)
        self.log_algorithm.setGeometry(QtCore.QRect(10, 0, 621, 411))
        self.log_algorithm.setObjectName("log_algorithm")
        self.tabWidget.addTab(self.matrix_graph, "")
        self.webEngine = QtWidgets.QWidget()
        self.webEngine.setObjectName("webEngine")
        self.tabWidget.addTab(self.webEngine, "")
        self.web = QWebEngineView(self.webEngine)

        self.retranslateUi(EnterMatrix)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(EnterMatrix.accept)
        self.buttonBox.rejected.connect(EnterMatrix.reject)
        QtCore.QMetaObject.connectSlotsByName(EnterMatrix)

    def retranslateUi(self, EnterMatrix):
        _translate = QtCore.QCoreApplication.translate
        EnterMatrix.setWindowTitle(_translate("EnterMatrix", "Граф :: Заповнення матриці"))
        self.generate.setText(_translate("EnterMatrix", "Виконувати"))
        self.graph.setText(_translate("EnterMatrix", "Вивести граф"))
        self.label.setText(_translate("EnterMatrix", "Введіть будьласка матрицю"))
        self.label_2.setText(_translate("EnterMatrix", "Результат роботи программи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.matrix_main), _translate("EnterMatrix", "Матриця"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.matrix_graph), _translate("EnterMatrix", "Логування роботи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.webEngine), _translate("EnterMatrix", "Перегляд графу"))

