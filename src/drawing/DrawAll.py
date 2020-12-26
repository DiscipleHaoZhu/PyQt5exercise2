'''

绘制各种图形

弧形
椭圆
矩形
多边形
绘制图像

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll,self).__init__()
        self.setWindowTitle('绘制各种图形')
        self.resize(300,600)

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(Qt.blue)
        # 绘制弧形
        rect = QRect(100,10,100,100)
        # alen：1个alen等于1/16度 。45度=45*16
        painter.drawArc(rect,0,50*16)
        # 绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(100,50,100,100, 0, 360 * 16)
        # 绘制带弦的弧
        painter.drawChord(100,170,100,100,12,130*16)
        # 绘制扇形
        painter.drawPie(100,240,100,100,12,130*16)
        # 绘制椭圆
        painter.drawEllipse(100,300,180,100)
        # 绘制5边形
        pot1 = QPoint(50, 400)
        pot2 = QPoint(100, 400)
        pot3 = QPoint(150, 450)
        pot4 = QPoint(120, 500)
        pot5 = QPoint(70, 530)
        polygon = QPolygon([pot1,pot2,pot3,pot4,pot5])
        painter.drawPolygon(polygon)
        # 绘制图形
        image = QImage('../Images/wrought1.jpg')
        rect = QRect(180,450,image.width()/3,image.height()/3)
        painter.drawImage(rect,image)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/pyc.ico'))
    main = DrawAll()
    main.show()

    sys.exit(app.exec_())