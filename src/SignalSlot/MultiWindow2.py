'''

多窗口交互（2）：使用信号和槽

如果一个窗口A与窗口B交互，A尽量不要直接访问B的控件，应该访问B的信号，
并指定与信号绑定的槽函数

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from NewDateDialog import NewDateDialog

class MultiWindow2(QWidget):
    def __init__(self):
        super(MultiWindow2, self).__init__()
        self.setWindowTitle('多窗口交互（2）：使用信号和槽')
        self.resize(400,100)

        self.open_btn = QPushButton('获取时间')
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接收子窗口内置信号的时间')
        self.lineEdit_emit.setText('接收子窗口自定义信号的时间')

        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.open_btn)

        self.setLayout(grid)

    def openDialog(self):
        dialog = NewDateDialog(self)
        # 连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        # 连接子窗口的自定义信号与主窗口的槽函数
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,dataStr):
        self.lineEdit_emit.setText(dataStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindow2()
    main.show()

    sys.exit(app.exec_())