import sys, os
sys.path.append(os.path.abspath('../'))
from PyQt5 import QtWidgets, QtGui
def HandleError(title, text="", informativetext="", detalis="", icon=""):
	"""
	This method is used to send pop-ups to the user, it can be both 
	errors and warnings, or information about success.
	"""
	if icon == "Information":
		icon = QtWidgets.QMessageBox.Information
	elif icon == "Warning":
		icon = QtWidgets.QMessageBox.Warning
	elif icon == "Question":
		icon = QtWidgets.QMessageBox.Question
	else:
		icon = QtWidgets.QMessageBox.Critical
	msg = QtWidgets.QMessageBox()
	msg.setWindowIcon(QtGui.QIcon('el_images/main.png'))
	msg.setIcon(icon)
	msg.setWindowTitle(title)
	msg.setText(text)
	msg.setInformativeText(informativetext)
	msg.setDetailedText(detalis)
	msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
	retval = msg.exec_()
