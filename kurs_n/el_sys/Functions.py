# -*- coding: utf-8 -*-

"""
Functions.py - Functions from work
Copyright 2018 Olena Horokhova
Distributed under GNU GPL v2 license. See license.txt for more infomation.

This software is provided 'as-is', 
without any express or implied warranty. 
In no event will the authors be held liable 
for any damages arising from the use of this software.
"""
from pathlib import Path
from PyQt5 import QtWidgets, QtGui

"""
Function used as a decorator to provide a class like Singleton
"""
def singleton(cls):
	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls()
		return instances[cls]
	return getinstance


"""
The Singleton class that works with the algorithm Floyd Warshal
"""
@singleton
class FloydWarshal:
	"""
	Initializes the base matrix in the appropriate sizes 
	numberofvertices - the number of vertices 
	(the matrix will be created as numberofvertices x numberofvertices)
	"""
	def __init__(self):
		self.numberofvertices = 0
		self.adjacencymatrix = None
		self.distancematrix = []


	"""
	The method of the class that fills the matrix
	"""
	def setData(self, adjacencymatrix=[]):
		self.adjacencymatrix = adjacencymatrix

	def setNumberOfVertices(self, numberofvertices):
		self.numberofvertices = int(numberofvertices)

	"""
	A class method that executes Floyd Worshell algorithm
	"""
	def algorithm(self):
		"""Nulled i=j"""
		if len(self.adjacencymatrix) == self.numberofvertices:
			for i in range(len(self.adjacencymatrix)):
				for j in range(len(self.adjacencymatrix[i])):
					if i == j:
						self.adjacencymatrix[i][j] = 0

		"""Load matrix in to new matrix"""
		self.distancematrix = self.adjacencymatrix
		if len(self.adjacencymatrix) == self.numberofvertices:
			"""Algorithm Floyd Warshal"""
			for k in range(self.numberofvertices):
				for i in range(len(self.distancematrix)):
					for j in range(len(self.distancematrix[i])):
						if self.distancematrix[i][k] + self.distancematrix[k][j] < self.distancematrix[i][j]:
							self.distancematrix[i][j] = self.distancematrix[i][k] + self.distancematrix[k][j]


"""
The method that opens the file and returns all of its data
"""
def load_html(file=None):
	html = Path(str(file))
	if(file is None):
		return "Sory but data file not found"
	elif(html.is_file()):
		try:
			f = open(str(file), encoding="utf8")
			data = f.read()
			f.close()
			return data
		except IOError:
			return "Sory but data file not found"
	else:
		return "Sory but data file not found"

"""
The method is used to display graphical errors, warnings, information, help
"""
def handle_error(title, text="", informativetext="", detalis="", icon=""):
	if icon == "Information":
		icon = QtWidgets.QMessageBox.Information
	elif icon == "Warning":
		icon = QtWidgets.QMessageBox.Warning
	elif icon == "Question":
		icon = QtWidgets.QMessageBox.Question
	else:
		icon = QtWidgets.QMessageBox.Critical
	msg = QtWidgets.QMessageBox()
	#msg.setIcon('../el_style/icon.png')
	msg.setWindowTitle(title)
	msg.setText(text)
	msg.setInformativeText(informativetext)
	msg.setDetailedText(detalis)
	msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
	retval = msg.exec_()