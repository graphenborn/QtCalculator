from PyQt6.QtCore import pyqtSlot
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

import sys

from GUI import Ui_MainWindow
from calculating import calculate

class Calculator (QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.num1 = ""
		self.numberBool = False
		self.num2 = ""
		self.operation = ""

		self.memory = ["Empty", "Empty", "Empty", "Empty", "Empty"]

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
		self.PiButton.pressed.connect(self.num_func)

		# Привязка функции к кнопке сброса
		self.cButton.pressed.connect(self.c_func)

		# Привязка кнопок операций к функциям
		self.plusButton.pressed.connect(self.operation_func)
		self.minusButton.pressed.connect(self.operation_func)
		self.multipleButton.pressed.connect(self.operation_func)
		self.divisionButton.pressed.connect(self.operation_func)
		self.equalsButton.pressed.connect(self.equals_func)
		self.sqrtButton.pressed.connect(self.sqrt_func)
		self.raiseButton.pressed.connect(self.operation_func)
		self.DmsButton.pressed.connect(self.sqrt_func)
		self.tenRaiseButton.pressed.connect(self.sqrt_func)
		self.tanhButton.pressed.connect(self.sqrt_func)
		self.LnButton.pressed.connect(self.sqrt_func)

		self.vscrollbar = self.scrollArea.verticalScrollBar()
		self.vscrollbar.rangeChanged.connect(self.scrollToBottom)
		self.negativeButton.pressed.connect(self.negative_func)

		#Привязка кнопок памяти
		self.MCButton_1.pressed.connect(self.MC_func)
		self.MCButton_2.pressed.connect(self.MC_func)
		self.MCButton_3.pressed.connect(self.MC_func)
		self.MCButton_4.pressed.connect(self.MC_func)
		self.MCButton_5.pressed.connect(self.MC_func)

		self.MRButton_1.pressed.connect(self.MR_func)
		self.MRButton_2.pressed.connect(self.MR_func)
		self.MRButton_3.pressed.connect(self.MR_func)
		self.MRButton_4.pressed.connect(self.MR_func)
		self.MRButton_5.pressed.connect(self.MR_func)

		self.MSButton_1.pressed.connect(self.MS_func)
		self.MSButton_2.pressed.connect(self.MS_func)
		self.MSButton_3.pressed.connect(self.MS_func)
		self.MSButton_4.pressed.connect(self.MS_func)
		self.MSButton_5.pressed.connect(self.MS_func)

		self.MPlustButton_1.pressed.connect(self.MPlus_func)
		self.MPlustButton_2.pressed.connect(self.MPlus_func)
		self.MPlustButton_3.pressed.connect(self.MPlus_func)
		self.MPlustButton_4.pressed.connect(self.MPlus_func)
		self.MPlustButton_5.pressed.connect(self.MPlus_func)

		self.MMinusButton_1.pressed.connect(self.MMinus_func)
		self.MMinusButton_2.pressed.connect(self.MMinus_func)
		self.MMinusButton_3.pressed.connect(self.MMinus_func)
		self.MMinusButton_4.pressed.connect(self.MMinus_func)
		self.MMinusButton_5.pressed.connect(self.MMinus_func)

	@pyqtSlot(int, int)
	def scrollToBottom(self,  minimum, maximum):
		self.vscrollbar.setValue(maximum)

	def MC_func(self):
		memIndex = int(self.sender().objectName()[-1]) - 1
		print(self.memory[memIndex])
		self.memory[memIndex] = "Empty"

	def MR_func(self):
		text = self.label.text().split()
		memIndex = int(self.sender().objectName()[-1]) - 1
		if text:
			if text[-1] == "<p>":
				self.label.setText(f'{self.label.text()} {self.memory[memIndex]} <p> ')
			elif text[-1].isdigit() or text[-1][0] == "-":
				text[-1] = (self.memory[memIndex])
				self.label.setText(" ".join(text))
			else:
				text.append(self.memory[memIndex])
				self.label.setText(" ".join(text))
		else:
			text.append(self.memory[memIndex])
			self.label.setText(" ".join(text))
		self.line_cleaning()

	def MS_func(self):
		text = self.label.text().split()
		memIndex = int(self.sender().objectName()[-1]) - 1
		if text[-1].isdigit():
			self.memory[memIndex] = text[-1]

	def MPlus_func(self):
		text = self.label.text().split()
		memIndex = int(self.sender().objectName()[-1]) - 1
		if text[-1].isdigit() or text[-1][0] == "-":
			if self.memory[memIndex] == "Empty":
				self.memory[memIndex] = text[-1]
			else:
				self.memory[memIndex] = str(int(self.memory[memIndex]) + int(text[-1]))

	def MMinus_func(self):
		text = self.label.text().split()
		memIndex = int(self.sender().objectName()[-1]) - 1
		if text[-1].isdigit() or text[-1][0] == "-":
			if self.memory[memIndex] == "Empty":
				if text[-1][0] == "-":
					self.memory[memIndex] = f"{text[-1]}"
				else:
					self.memory[memIndex] = f"-{text[-1]}"
			else:
				self.memory[memIndex] = str(int(self.memory[memIndex]) - int(text[-1]))

	def c_func(self):
		self.num1 = ""
		self.num2 = ""
		self.operation = ""
		self.label.setText("")

	def num_func(self):
		number = self.sender().text()
		if self.numberBool:
			self.label.setText(f'{self.label.text()}{number}')
		else:
			self.label.setText(f'{self.label.text()}{number}')

	def change_num(self):
		self.numberBool = not self.numberBool

	def sqrt_func(self):
		text = self.label.text().split()
		self.operation = self.sender().text()
		self.num2 = 0
		self.num1 = text[-1]
		text[-1] = f'{self.operation} {text[-1]}'
		self.label.setText(" ".join(text))
		result = calculate(self.num1, self.operation, self.num2)
		self.label.setText(f'{self.label.text()} <p> = {result} <p> ')
		self.change_num()
		self.num1 = ""
		self.num2 = ""
		self.operation = ""
		self.line_cleaning()

	def operation_func(self):
		self.change_num()
		self.operation = self.sender().text()
		self.label.setText(f'{self.label.text()} {self.operation} ')

	def line_cleaning(self):
		ID = self.IDEdit.text()
		IDSum = 0
		for i in ID:
			IDSum+=int(i)
		if len(str(IDSum)) > 1:
			x = 0
			for i in str(IDSum):
				x += int(i)
			IDSum = x
		lines = self.label.text().split("<p>")
		countLines = len(lines)
		while countLines > IDSum:
			lines.pop(0)
			countLines = len(lines)
		self.label.setText("<p>".join(lines))

	def negative_func(self):
		text = self.label.text().split()
		if text[-1].isdigit():
			if "-" in text[-1]:
				text[-1] = text[-1][1:]
			else:
				text[-1] = "-" + text[-1]
			self.label.setText(" ".join(text))


	def equals_func(self):
		nums = self.label.text().split()
		self.num1 = nums[-3]
		self.num2 = nums[-1]
		result = calculate(self.num1, self.operation, self.num2)
		self.label.setText(f'{self.label.text()} <p> = {result} <p> ')
		self.change_num()
		self.num1 = ""
		self.num2 = ""
		self.operation = ""
		self.line_cleaning()


app = QApplication(sys.argv)
window = Calculator()

window.show()
app.exec()