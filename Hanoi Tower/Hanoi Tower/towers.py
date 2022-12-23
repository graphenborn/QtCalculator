# -*- coding: utf-8 -*-

# На каждом шпинделе надеты диски, в количестве, равном соответствующей
# цифре из ID студента. Все диски имеют разные диаметры. Диаметр диска
# равен M * 10 + N, где М – номер шпинделя, на котором надет диск,
# а N – это номер диска на шпинделе, считая сверху вниз.

import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen, QFont
from PyQt6.QtCore import QRect, Qt

# Генератор цвета
def get_colors(num):
    colors = []
    for _ in range(num):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        colors.append(rgb)
    return colors

# Присваиваем цвета дискам
def set_colors(towers, id):
    color_dict = {}
    num = 0

    for i in id:
        num += i    # Всего дисков
    
    colors = get_colors(num)

    num = 0
    for tower in towers:
        for disk in tower:
            color_dict[disk.width()] = colors[num]
            num += 1
    return color_dict


class Towers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 1250, 400)
        self.center()

        self.id = [7, 0, 1, 7, 4, 4, 6, 4]
        self.towers = self.init_towers()
        self.color_dict = set_colors(self.towers, self.id)

        self.move_disk(0, 1)
        self.move_disk(0, 1)


    # Центрирование окна
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())   


    def init_towers(self):
        objects = []

        # Начальная позиция на оси х (для основ башен)
        x = 50

        # Счетчик дисков (для распределения цветов
        # и заранее сгенерированного списка)
        disk_num = 0
        
        # Цикл по шпинделям
        for tower in range(1, 9):

            # начальная позиция для шпинделя (вертикальная палка)
            x2 = x + 47 

            # Кол-во дисков на данном шпинделе (берётся из id студента)
            n = self.id[tower - 1]

            # Начальная позиция по оси y для дисков
            y = 340

            # Отрисовка дисков
            # (обратный цикл: от основания шпинделя к вершине)
            disks = []
            for i in range(n, 0, -1):
                
                # Диаметр диска по формуле
                diameter = tower * 10 + i

                # половина диаметра для расположения диска по
                # центру шпинделя +\- погрешность в 2 единицы
                half_diameter = round(diameter / 2) - 2

                disk_num += 1
                rect = QRect(x2 - half_diameter, y, diameter, 10)
                disks.append(rect)

                # смещаемся вверх по оси y
                y -= 10
            objects.append(disks)
            # смещаемся вправо по оси x
            x += 150
        return objects


    def move_disk(self, t1, t2):
        from_tower = self.towers[t1]

        if not from_tower:
            mes = f"На шпинделе №{t1+1} нет дисков."
            print(mes)
            return mes
        
        to_tower = self.towers[t2]
        y = 340 # стартовая координата для дисков
        
        # Есть ли диски на втором шпинделе
        if to_tower:
            last_disk = to_tower[-1]
            y = last_disk.y() - 10
            disk = from_tower[-1]  # последний диск
            if last_disk.width() < disk.width():
                mes = f"На шпинделе №{t2+1} последний диск меньше перемещаемого диска."
                print(mes)
                return mes

        disk = from_tower.pop()   # последний диск
        new_x = disk.x() + 150

        disk.moveTo(new_x, y)
        to_tower.append(disk)


    # Отрисовка башен и дисков
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 1))

        # Начальная позиция на оси х (для основ башен)
        x = 50

        # Счетчик дисков (для распределения цветов
        # и заранее сгенерированного списка)
        disk_num = 0
        
        # Цикл по шпинделям
        for t in range(len(self.towers)):
            tower = self.towers[t]
            # начальная позиция для шпинделя (вертикальная палка)
            x2 = x + 47 
            start_y = 350

            # Заливка шпинделей
            painter.setBrush(QBrush(Qt.GlobalColor.gray))

            # Отрисовка шпинделя
            painter.drawRects(
                QRect(x, start_y, 100, 10),
                QRect(x2, start_y, 5, -300)
            )

            # Отрисовка дисков
            for d in range(len(tower)):
                disk = tower[d]
                diameter = disk.width()

                # присваиваем заранее сгенерованный цвет данному диску
                r, g, b = self.color_dict[diameter]
                disk_num += 1

                painter.setBrush(QBrush(QColor(r, g, b)))
                painter.drawRect(disk)

                # вписываем значение диаметра диска
                self.drawText(disk, painter, str(diameter))
            x += 150


    # Вставка значения диаметра диска
    def drawText(self, rect, painter, d):
        painter.setFont(QFont('Arial', 8, weight=QFont.Weight.Bold))
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, d)


app = QApplication(sys.argv)
win = Towers()
win.show()

sys.exit(app.exec())
