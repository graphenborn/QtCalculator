# -*- coding: utf-8 -*-

# На каждом шпинделе надеты диски, в количестве, равном соответствующей
# цифре из ID студента. Все диски имеют разные диаметры. Диаметр диска
# равен M * 10 + N, где М – номер шпинделя, на котором надет диск,
# а N – это номер диска на шпинделе, считая сверху вниз.

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
from PyQt6.QtCore import QPoint, QRect, Qt


class Towers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 1250, 400)
        self.center()
        self.id = [7, 0, 1, 7, 4, 4, 6, 4]


    # Центрирование окна
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())   

    # Отрисовка башен
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 1))
        pos = 50
        for t in range(1, 9):
            pos2 = pos + 40
            painter.setBrush(QBrush(Qt.GlobalColor.gray))
            painter.drawRects(
                QRect(pos, 250, 90, 10),
                QRect(pos2, 250, 10, -100)
            )
            
            n = self.id[t - 1]
            y = 240
            diameter = t * 10

            # Отрисовка дисков
            for i in range(n, 0, -1):
                d = diameter + i
                painter.setBrush(QBrush(Qt.GlobalColor.red))
                painter.drawRect(pos2 - d/2, y, d, 10)
                y -= 10

            pos += 150


app = QApplication(sys.argv)
win = Towers()
win.show()

sys.exit(app.exec())
