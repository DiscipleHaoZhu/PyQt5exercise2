'''

信号与槽自动连接
设置连接的槽名称匹配
self.okButton1.setObjectName('cancelButton')
cliked为按键自带的信号名
槽函数名称应符合下面结构：
on_cancelButton_clicked

'''

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.setWindowTitle('信号与槽自动连接')
        self.okButton = QPushButton('ok',self)
        self.okButton.setObjectName('okButton')

        self.okButton1 = QPushButton('cancelButton',self)
        self.okButton1.setObjectName('cancelButton')

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.okButton1)
        self.setLayout(layout)

        QtCore.QMetaObject.connectSlotsByName(self)
        #self.okButton.clicked.connect(self.on_okButton_clicked)
    @QtCore.pyqtSlot()
    def on_okButton_clicke(self):
        print('点击了ok按钮')

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancelButton按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSignalSlot()
    main.show()

    sys.exit(app.exec_())