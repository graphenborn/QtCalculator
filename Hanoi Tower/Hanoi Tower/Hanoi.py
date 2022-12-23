from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QBrush, QPen
from PyQt6.QtCore import Qt

from GUI import Ui_MainWindow

import sys

class Hanoi (QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 10, Qt.PenStyle.SolidLine))

        painter.drawRect(10, 20, 80, 60)

app = QApplication(sys.argv)
window = Hanoi()

window.show()
app.exec()