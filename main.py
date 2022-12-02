from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication

import sys

from GUI import Ui_MainWindow

class Calculator (QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.num1 = ""
		self.numberBool = False
		self.num2 = ""
		self.operation = None

		# Привязка функции ввода числа к кнопкам
		self.oneButton.pressed.connect(self.num_func)
		self.twoButton.pressed.connect(self.num_func)
		self.threeButton.pressed.connect(self.num_func)
		self.zeroButton.pressed.connect(self.num_func)
		self.fourButton.pressed.connect(self.num_func)
		self.fiveButton.pressed.connect(self.num_func)
		self.sixButton.pressed.connect(self.num_func)
		self.sevenButton.pressed.connect(self.num_func)
		self.eightButton.pressed.connect(self.num_func)
		self.nineButton.pressed.connect(self.num_func)
		self.dotButton.pressed.connect(self.num_func)

		# Привязка функции к кнопке сброса
		self.cButton.pressed.connect(self.c_func)

	def c_func(self):
		self.num1 = None
		self.num2 = None
		self.operation = None
		self.lineEdit.setText("")

	def num_func(self):
		number = self.sender().text()
		if self.numberBool:
			self.num2+=number
			self.lineEdit.setText(f"{self.num2}")
		else:
			self.num1+=number
			self.lineEdit.setText(f"{self.num1}")

	def change_num(self):
		self.numberBool = True
		self.lineEdit.setText("")


app = QApplication(sys.argv)
window = Calculator()

window.show()
app.exec()