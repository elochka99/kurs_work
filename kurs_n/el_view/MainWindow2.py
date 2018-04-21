# -*- coding: utf-8 -*-

"""
MainWindow.py - Program
Copyright 2018 Olena Horokhova
Distributed under GNU GPL v2 license. See license.txt for more infomation.

This software is provided 'as-is', 
without any express or implied warranty. 
In no event will the authors be held liable 
for any damages arising from the use of this software.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tab.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.tab.setMinimumSize(QtCore.QSize(640, 480))
        self.tab.setMaximumSize(QtCore.QSize(640, 480))
        self.tab.setObjectName("tab")
        self.main_index = QtWidgets.QWidget()
        self.main_index.setObjectName("main_index")
        self.three = QtWidgets.QRadioButton(self.main_index)
        self.three.setGeometry(QtCore.QRect(30, 10, 231, 17))
        self.three.setChecked(True)
        self.three.setObjectName("three")
        self.four = QtWidgets.QRadioButton(self.main_index)
        self.four.setGeometry(QtCore.QRect(30, 40, 231, 17))
        self.four.setObjectName("four")
        self.five = QtWidgets.QRadioButton(self.main_index)
        self.five.setGeometry(QtCore.QRect(30, 70, 231, 17))
        self.five.setObjectName("five")
        self.six = QtWidgets.QRadioButton(self.main_index)
        self.six.setGeometry(QtCore.QRect(30, 100, 231, 17))
        self.six.setObjectName("six")
        self.main_generate = QtWidgets.QPushButton(self.main_index)
        self.main_generate.setGeometry(QtCore.QRect(30, 130, 231, 23))
        self.main_generate.setObjectName("main_generate")
        self.main_index_info = QtWidgets.QTextBrowser(self.main_index)
        self.main_index_info.setGeometry(QtCore.QRect(305, 10, 321, 431))
        self.main_index_info.setObjectName("main_index_info")
        self.tab.addTab(self.main_index, "")
        self.main_about_algorithm = QtWidgets.QWidget()
        self.main_about_algorithm.setObjectName("main_about_algorithm")
        self.about_algorithm = QtWidgets.QTextBrowser(self.main_about_algorithm)
        self.about_algorithm.setGeometry(QtCore.QRect(0, 0, 636, 456))
        self.about_algorithm.setMinimumSize(QtCore.QSize(636, 456))
        self.about_algorithm.setMaximumSize(QtCore.QSize(636, 456))
        self.about_algorithm.setObjectName("about_algorithm")
        self.tab.addTab(self.main_about_algorithm, "")
        self.main_about_program = QtWidgets.QWidget()
        self.main_about_program.setObjectName("main_about_program")
        self.about_program = QtWidgets.QTextBrowser(self.main_about_program)
        self.about_program.setGeometry(QtCore.QRect(0, 0, 636, 456))
        self.about_program.setMinimumSize(QtCore.QSize(636, 456))
        self.about_program.setMaximumSize(QtCore.QSize(636, 456))
        self.about_program.setObjectName("about_program")
        self.tab.addTab(self.main_about_program, "")
        self.main_about_author = QtWidgets.QWidget()
        self.main_about_author.setObjectName("main_about_author")
        self.about_author = QtWidgets.QTextBrowser(self.main_about_author)
        self.about_author.setGeometry(QtCore.QRect(0, 0, 636, 456))
        self.about_author.setMinimumSize(QtCore.QSize(636, 456))
        self.about_author.setMaximumSize(QtCore.QSize(636, 456))
        self.about_author.setObjectName("about_author")
        self.tab.addTab(self.main_about_author, "")
        self.main_about_license = QtWidgets.QWidget()
        self.main_about_license.setObjectName("main_about_license")
        self.about_license = QtWidgets.QTextBrowser(self.main_about_license)
        self.about_license.setGeometry(QtCore.QRect(0, 0, 636, 456))
        self.about_license.setMinimumSize(QtCore.QSize(636, 456))
        self.about_license.setMaximumSize(QtCore.QSize(636, 456))
        self.about_license.setObjectName("about_license")
        self.tab.addTab(self.main_about_license, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Граф :: Головне меню"))
        self.three.setText(_translate("MainWindow", "Матриця розімром 3х3"))
        self.four.setText(_translate("MainWindow", "Матриця розміром 4х4"))
        self.five.setText(_translate("MainWindow", "Матриця розміром 5х5"))
        self.six.setText(_translate("MainWindow", "Матриця розміром 6х6"))
        self.main_generate.setText(_translate("MainWindow", "Генерувати матрицю"))
        self.tab.setTabText(self.tab.indexOf(self.main_index), _translate("MainWindow", "Головна"))
        self.tab.setTabText(self.tab.indexOf(self.main_about_algorithm), _translate("MainWindow", "Про алгоритм"))
        self.tab.setTabText(self.tab.indexOf(self.main_about_program), _translate("MainWindow", "Про програму"))
        self.tab.setTabText(self.tab.indexOf(self.main_about_author), _translate("MainWindow", "Автор"))
        self.tab.setTabText(self.tab.indexOf(self.main_about_license), _translate("MainWindow", "Ліцензія"))