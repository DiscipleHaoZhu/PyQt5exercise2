'''

设置窗口样式：主要是窗口边框、标题栏以及窗口本身的样式

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class WindowPattern(QMainWindow):
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.setWindowTitle('设置窗口样式')
        self.resize(500,260)
        # 仅显示窗口最大化按钮
        #self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet("#MainWindow{border-image:url(../Images/board.jpg);}")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowPattern()
    main.show()

    sys.exit(app.exec_())