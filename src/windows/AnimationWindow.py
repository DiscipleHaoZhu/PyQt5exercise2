'''

实现不规则窗口的动画实现

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class AnimationWindow(QWidget):
    def __init__(self,parent=None):
        super(AnimationWindow, self).__init__(parent)
        self.i = 1
        self.mypix()
        self.timer = QTimer()
        self.timer.setInterval(500)  # 500毫秒
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    # 显示不规则pic
    def mypix(self):
        self.update()
        if self.i == 5:
            self.i = 1
        self.mypic = {1: '../Images/Sample1.png', 2: '../Images/Sample2.png', 3: '../Images/Sample3.png', 4: '../Images/Sample4.png'}
#        self.mypic = {1: '../Images/包包/bag0.png', 2: '../Images/包包/bag1.png', 3: '../Images/包包/bag2.png', 4: '../Images/包包/bag3.png'}

        self.pix = QPixmap(self.mypic[self.i])
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition = None

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
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    # 双击事件
    def mouseDoubleClickEvent(self, QMouseEv):
        if QMouseEv.button() == 1:
            self.i += 1
            self.mypix()

    def timeChange(self):
        self.i += 1
        self.mypix()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AnimationWindow()
    main.show()

    sys.exit(app.exec_())