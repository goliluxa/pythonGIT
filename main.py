import sys

import os
from PIL import Image, ImageDraw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import random as r

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        b = 240
        new_image = Image.new("RGB", (200, 200), (b, b, b))
        drawer = ImageDraw.Draw(new_image)
        a = r.randrange(10, 100)
        drawer.ellipse(((a, a), (200 - a, 200 - a)), '#FFDB00')
        new_image.save('cik.png')

        self.pixmap = QPixmap('cik.png')
        self.image = QLabel(self)
        self.image.move(40, 10)
        self.image.resize(200, 200)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        os.remove('cik.png')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
