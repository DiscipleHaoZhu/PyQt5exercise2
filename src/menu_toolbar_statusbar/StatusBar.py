'''

创建和使用状态栏

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusbarDemo(QMainWindow):
    def __init__(self):
        super(StatusbarDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('状态栏例子')
        self.resize(400,300)
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.processTrigger)
        #self.setCentralWidget(QTextEdit())
        self.ssss = QStatusBar()
        self.setStatusBar(self.ssss)

    def processTrigger(self,q):
        if q.text() == 'show':
            self.ssss.showMessage(q.text() + '菜单被点击了',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/pyc.ico'))
    main = StatusbarDemo()
    main.show()

    sys.exit(app.exec_())