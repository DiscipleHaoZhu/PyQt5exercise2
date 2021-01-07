'''

使用Partial对象为槽函数传递参数

'''

from PyQt5.QtWidgets import *
from functools import partial
import sys

class PartialSlotArg(QMainWindow):
    def __init__(self):
        super(PartialSlotArg, self).__init__()
        self.setWindowTitle("使用Partial对象为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        ddf = -253.5
        button1.clicked.connect(partial(self.onButtonClick,10,ddf))
        button2.clicked.connect(partial(self.onButtonClick,50, -2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self,m,n):
        print('m + n = ',m+n)
        QMessageBox.information(self,'结果',str(m+n))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PartialSlotArg()
    main.show()

    sys.exit(app.exec_())
