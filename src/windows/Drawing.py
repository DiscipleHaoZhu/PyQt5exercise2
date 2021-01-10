'''

项目实战：实现绘图应用

需要解决3个核心内容
1.如何绘图
在paintEvent方法中绘图，通过调用update方法触发painEvent的调用

2.在哪里绘图
在白色背景的QPixmap对象中绘图

3.如何通过移动鼠标进行绘图
鼠标3个事件
a.鼠标按下：mousePressEvent
b.鼠标移动：mouseMoveEvent
c.鼠标抬起：mouseReleaseEvent

'''

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPainter,QPixmap
import sys

class Drawing(QWidget):
    def __init__(self):
        super(Drawing, self).__init__()
        self.setWindowTitle('实现绘图应用')

        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        # 画布大小为400*400，背景为白色
        self.pix = QPixmap(600,600)
        self.pix.fill(Qt.blue)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # 根据鼠标指针前后两个位置绘制直线
        pp.drawLine(self.lastPoint,self.endPoint)
        # 让前一个坐标值等于后一段的起点，实现连续划线
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            # 触发event，并获取当前位置
            self.lastPoint = event.pos()

    def mouseMoveEvent(self,event):
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            self.update()


    def mouseReleaseEvent(self,event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Drawing()
    main.show()

    sys.exit(app.exec_())