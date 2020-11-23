import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
import math


class Example(QWidget):
    def __init__(self):
        super().__init__()
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def drawRectangles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        size = randint(1, 3)
        qp.drawEllipse(10, 15, 20 * size, 20 * size)
        size = randint(1, 3)
        qp.drawEllipse(130, 400, 20 * size, 20 * size)
        size = randint(1, 3)
        qp.drawEllipse(600, 200, 20 * size, 20 * size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
