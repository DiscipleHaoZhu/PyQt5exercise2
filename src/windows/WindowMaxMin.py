'''

用代码控制窗口的最大化和最小化

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class WindowMaxMin(QWidget):
    def __init__(self):
        super(WindowMaxMin, self).__init__()
        self.setWindowTitle('用代码控制窗口的最大化和最小化')
        self.resize(300,400)

        layout = QVBoxLayout()
        maxButton1 = QPushButton('窗口最大化1')
        maxButton1.clicked.connect(self.maximized1)

        maxButton2 = QPushButton('窗口最大化2')
        maxButton2.clicked.connect(self.maximized1)
        maxButton2.clicked.connect(self.showMaximized)

        minButton = QPushButton('窗口最小化')
        minButton.clicked.connect(self.maximized1)
        minButton.clicked.connect(self.showMinimized)

        layout.addWidget(maxButton1)
        layout.addWidget(maxButton2)
        layout.addWidget(minButton)
        self.setLayout(layout)

    def maximized1(self):
        desktop = QApplication.desktop()
        # 获取桌面可用存储
        rect = desktop.availableGeometry()
        self.setGeometry(rect)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WindowMaxMin()
    main.show()

    sys.exit(app.exec_())