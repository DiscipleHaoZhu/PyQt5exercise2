'''

用画刷填充区域
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class FillRect(QWidget):
    def __init__(self):
        super(FillRect,self).__init__()
        self.setWindowTitle('绘制各种图形')
        self.resize(300,600)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)

        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,15,90,60)

        brush = QBrush(Qt.DragCopyCursor)
        painter.setBrush(brush)
        painter.drawRect(130,15,90,60)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/pyc.ico'))
    main = FillRect()
    main.show()

    sys.exit(app.exec_())