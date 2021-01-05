'''
垂直盒布局（QVBoxLayout）

'''

import sys,math
from PyQt5.QtWidgets import *

class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle('垂直盒布局')

        hlayout = QVBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))
        # 设置按钮间距
        hlayout.setSpacing(70)
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VBoxLayout()
    main.show()
    sys.exit(app.exec_())