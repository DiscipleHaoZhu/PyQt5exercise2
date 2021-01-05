'''

设置伸缩量

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Stretch(QWidget):
    def __init__(self):
        super(Stretch, self).__init__()
        self.setWindowTitle('设置伸缩量')
        self.resize(700,300)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('按钮1')
        btn2.setText('按钮2')
        btn3.setText('按钮3')

        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(btn1)
        layout.addStretch(2)
        layout.addWidget(btn2)
        layout.addStretch(3)
        layout.addWidget(btn3)

        btn11 = QPushButton(self)
        btn12 = QPushButton(self)
        btn13 = QPushButton(self)
        btn14 = QPushButton('确定')
        btn15 = QPushButton('取消')
        btn11.setText('按钮11')
        btn12.setText('按钮12')
        btn13.setText('按钮13')

        layout1 = QHBoxLayout()
        layout1.addStretch(0)
        layout1.addWidget(btn11)
        layout1.addWidget(btn12)
        layout1.addWidget(btn13)
        layout1.addStretch(1)
        layout1.addWidget(btn14)
        layout1.addWidget(btn15)

        vlayout = QVBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addLayout(layout1)

        self.setLayout(vlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.show()
    sys.exit(app.exec_())