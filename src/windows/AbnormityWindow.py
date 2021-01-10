'''

实现不规则窗口（异形窗口）

通过mask实现异形窗口

需要一张通明的png图，透明部分被扣出，形成一个非规矩的区域

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()
        self.setWindowTitle('异形窗口')
#        self.pix = QBitmap('../Images/wrought1.jpg')
        self.pix = QPixmap('../Images/Address Book.png')

        self.resize(self.pix.size())
#        self.setMask(self.pix)
        self.setMask(self.pix.mask())


    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            # 触发event，并获取当前位置
            self.m_drag = True

            self.m_DragPosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))

            print(event.globalPos())
            print(event.pos())
            print(self.pos())

        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self,QMouseEve):
        if self.m_drag and Qt.LeftButton:
            # 当左键移动窗体时修改偏移值，左上角坐标
            self.move(QMouseEve.globalPos() - self.m_DragPosition)


    def mouseReleaseEvent(self,QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def paintEvent(self, event):
        painter = QPainter(self)
#        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('../Images/floor tile1.jpg'))
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbnormityWindow()
    main.show()

    sys.exit(app.exec_())