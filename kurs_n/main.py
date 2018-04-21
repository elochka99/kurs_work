#-*- coding: utf-8 -*-

"""
main.py - Program
Copyright 2018 Olena Horokhova
Distributed under GNU GPL v2 license. See license.txt for more infomation.

This software is provided 'as-is',
without any express or implied warranty.
In no event will the authors be held liable
for any damages arising from the use of this software.
"""
import sys
import pyqtgraph as pg
from os import system
from el_sys.Functions import (singleton, FloydWarshal, load_html, handle_error)
from el_view import (MainWindow, Graph)
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

@singleton
class Engine:
    __app = None
    __MainWindow = None
    __Graph = None
    __El_Window = None
    __El_Dialog = None
    __El_FloydWarshal = None


    def __init__(self):
        if self.__app is None:
            self.__app = QtWidgets.QApplication(sys.argv)
        if self.__MainWindow is None:
            self.__MainWindow = MainWindow.Ui_MainWindow()
        if self.__Graph is None:
            self.__Graph = Graph.Ui_EnterMatrix()
        if self.__El_Window is None:
            self.__El_Window = QtWidgets.QMainWindow()
            self.__El_Window.setWindowIcon(QtGui.QIcon('el_style/icon.png'))
        if self.__El_Dialog is None:
            self.__El_Dialog = QtWidgets.QDialog()
            self.__El_Dialog.setWindowIcon(QtGui.QIcon('el_style/icon.png'))
        if self.__El_FloydWarshal is None:
            self.__El_FloydWarshal = FloydWarshal()


    def showMainWindow(self):
        self.__MainWindow.setupUi(self.__El_Window)
        self.MainWindowSetData()
        self.__El_Window.show()
        sys.exit(self.__app.exec_())

    def MainWindowSetData(self):
        self.__MainWindow.about_license.setHtml(load_html("el_style/license.html"))
        self.__MainWindow.about_author.setHtml(load_html("el_style/author.html"))
        self.__MainWindow.about_algorithm.setHtml(load_html("el_style/algorithm.html"))
        self.__MainWindow.main_index_info.setHtml(load_html("el_style/info.html"))
        self.__MainWindow.about_program.setHtml(load_html("el_style/program.html"))
        self.__MainWindow.main_generate.clicked.connect(self.MainWindowButtonGenerate)

    def MainWindowButtonGenerate(self):
        try:
            if(int(self.__MainWindow.size.text()) < 3):
                handle_error("Граф::Помилка", "Виникла помилка розміру", "Вибачте але розмір матриці має бути від 3 і більше елементів", "")
            else:
                self.showGraphWindow(int(self.__MainWindow.size.text()))
        except ValueError:
            handle_error("Граф::Помилка", "Виникла помилка введення", "Вибачте але розмір матриці має бути цілочисельного значення 0...N", "")

        #if self.__MainWindow.three.isChecked():
        #    self.showGraphWindow(3)
        #elif self.__MainWindow.four.isChecked():
        #    self.showGraphWindow(4)
        #elif self.__MainWindow.five.isChecked():
        #    self.showGraphWindow(5)
        #elif self.__MainWindow.six.isChecked():
        #    self.showGraphWindow(6)
        #else:
        #    handle_error("Граф::Помилка", "Виникла помилка при виборі", "Вибачте але на данний момент программа підтримує "\
        #        "можливість працювати тільки з матрицями 3х3, 4х4, 5х5, 6х6", "")


    #"""ALL METHODS FROM FILE el_view/Graph.py"""
    def showGraphWindow(self, number):
        self.__Graph.setupUi(self.__El_Dialog)
        self.GraphWindowSetData(int(number))
        self.__El_Dialog.show()

    
    def GraphWindowSetData(self, number):
        self.__El_FloydWarshal.numberofvertices = int(number)
        self.__Graph.log_algorithm.clear()
        self.__Graph.matrix.setRowCount(int(number))
        self.__Graph.matrix.setColumnCount(int(number))
        self.__Graph.newmatrix.setRowCount(int(number))
        self.__Graph.newmatrix.setColumnCount(int(number))
        self.__Graph.log_algorithm.append(str("Create Matrix:"))
        for i in range(int(number)):
            self.__Graph.matrix.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            self.__Graph.newmatrix.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            for j in range(int(number)):
                self.__Graph.matrix.setItem(i, j, QtWidgets.QTableWidgetItem("0"))
                self.__Graph.newmatrix.setItem(i, j, QtWidgets.QTableWidgetItem("0"))
                self.__Graph.log_algorithm.append(str("MATRIX[" + str(i) + "]["+str(j)+"]=0"))
        self.__Graph.newmatrix.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.__Graph.generate.clicked.connect(self.GraphWindowGenNewMatrix)
        self.__Graph.graph.clicked.connect(self.PyQtGraphMain)

    def GraphWindowGenNewMatrix(self):
        self.__Graph.log_algorithm.append(str("Algorithm FloydWarshal"))
        tmp_matrix = []
        for i in range(self.__Graph.matrix.rowCount()):
            tmp_column = []
            for j in range(self.__Graph.matrix.columnCount()):
                try:
                    tmp_column.append(int(self.__Graph.matrix.item(i, j).text()))
                except ValueError:
                    tmp_column.append(0)
            tmp_matrix.append(tmp_column)
        print(tmp_matrix)
        self.__El_FloydWarshal.setData(tmp_matrix)
        self.__El_FloydWarshal.algorithm()
        print(self.__El_FloydWarshal.distancematrix)
        for i in range(self.__Graph.matrix.rowCount()):
            for j in range(self.__Graph.matrix.columnCount()):
                self.__Graph.newmatrix.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.__El_FloydWarshal.distancematrix[i][j])))
                self.__Graph.log_algorithm.append(str("MATRIX[" + str(i) + "]["+str(j)+"]=" + str(self.__El_FloydWarshal.distancematrix[i][j])))
        

    def PyQtGraphMain(self):
        string = ""
        for i in range(self.__El_FloydWarshal.numberofvertices):
            for j in range(self.__El_FloydWarshal.numberofvertices):
                string = string + str(self.__El_FloydWarshal.distancematrix[i][j]) + ', '
            string = string + '\\n'
        print(string)
        self.__Graph.web.setHtml(load_html("el_style/create_graph.html") + '<script type="text/javascript">application.SetAdjacencyMatrix("' + string + '");</script>"')
        """<script type="text/javascript">application.SetAdjacencyMatrix("0, 0, 3, 0, \n4, 0, 1, 3, \n1, 0, 0, 0,\n 0, 0, 3, 4,");</script>"""        


if __name__ == '__main__':
    if ('PyQt5' not in sys.modules):
        print('PyQT5 Not installed\n Use "pip3 install pyqt5" from use this program')
        print('Or "/patch/to/python.exe -m pip install pyqt5"')
        print('From open Terminal (PowerShell) use WIN + X and choise PowerShell with Root')
        system("pause")
        exit()
    if ('pyqtgraph' not in sys.modules):
        print('PyQtGraph Not installed\n Use "pip3 install pyqtgraph" from use this program')
        print('Or "/patch/to/python.exe -m pip install pyqtgraph"')
        print('From open Terminal (PowerShell) use WIN + X and choise PowerShell with Root')
        system("pause")
        exit()
    El_Engine = Engine()
    El_Engine.showMainWindow()
