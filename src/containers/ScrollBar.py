'''

滚动条（QScrollBar）

QScrollBar的作用
1.通过滚动条值得变化控制其他控件状态的变化
2.通过滚动条值得变化控制控件位置的变化

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollBar(QWidget):
    def __init__(self,parent=None):
        super(ScrollBar, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滚动条（QScrollBar）')
        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条去改变文字颜色')

        hbox.addWidget(self.label)

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        #self.scrollbar4.setOrientation(Qt.Horizontal)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)

        hbox.addWidget(self.scrollbar1)
        hbox.addWidget(self.scrollbar2)
        hbox.addWidget(self.scrollbar3)
        hbox.addWidget(self.scrollbar4)

        self.setGeometry(300,300,300,200)

        self.setLayout(hbox)

        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrollbar1.value(),self.scrollbar2.value(),self.scrollbar3.value())
        # 创建调色板
        palette = QPalette()
        # 设置颜色R+G+B+透明度
        col = QColor(self.scrollbar1.value(),self.scrollbar2.value(),self.scrollbar3.value(),255)
        palette.setColor(QPalette.Foreground,col)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        self.label.move(self.label.x(),self.y + self.scrollbar4.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ScrollBar()
    gui.show()
    app.exec_()