'''

让按钮永远在右下方

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class RightBottomButton(QWidget):
    def __init__(self):
        super(RightBottomButton, self).__init__()
        self.setWindowTitle('让按钮永远在右下方')
        self.resize(400,300)

        okButton = QPushButton('确定')
        cancelButton = QPushButton('取消')

        hlayout = QHBoxLayout()
        hlayout.addStretch(1)
        hlayout.addWidget(okButton)
        hlayout.addWidget(cancelButton)

        vbox = QVBoxLayout()

        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')

        #vbox.addStretch(1)
        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        vbox.addStretch(1)
        vbox.addLayout(hlayout)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = RightBottomButton()
    main.show()
    sys.exit(app.exec_())