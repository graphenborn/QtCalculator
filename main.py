from PyQt6 import QtCore
from PyQt6.QtCore import Qt
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

		self.plusButton.pressed.connect(self.plus_func)

		self.equalsButton.pressed.connect(self.equals_func)

	def c_func(self):
		self.num1 = None
		self.num2 = None
		self.operation = None
		self.textEdit.setText("")

	def num_func(self):
		number = self.sender().text()
		if self.numberBool:
			self.num2+=number
			self.textEdit.insertPlainText(number)
		else:
			self.num1+=number
			self.textEdit.insertPlainText(number)

	def change_num(self):
		self.numberBool = not self.numberBool

	def plus_func(self):
		self.change_num()
		self.textEdit.insertPlainText(" + ")
		self.operation = "Plus"

	def equals_func(self):
		self.textEdit.insertPlainText("\n = ")
		print(self.num1, self.num2, self.operation)


app = QApplication(sys.argv)
window = Calculator()

window.show()
app.exec()