'''

设置窗口风格：控件风格

QApplication.setStyle()

'''
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WindowStytle(QWidget):
    def __init__(self):
        super(WindowStytle, self).__init__()
        self.setWindowTitle('设置窗口风格')
        #self.resize(300,200)

        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel('设置窗口风格')
        self.combox = QComboBox()
        self.combox.addItems(QStyleFactory.keys())
        #print(QStyleFactory.keys())
        # 获取当前窗口的风格
        print(QApplication.style().objectName())
        index = self.combox.findText(QApplication.style().objectName(),QtCore.Qt.MatchExactly)
        self.combox.setCurrentIndex(index)
        self.combox.activated[str].connect(self.handleStyleChanged)

        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.combox)
        self.setLayout(horizontalLayout)

    def handleStyleChanged(self,style):
        QApplication.setStyle(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowStytle()
    main.show()

    sys.exit(app.exec_())