'''

使用QSS为标签和按钮添加背景图

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPainter,QPixmap,QMovie
import sys

class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet('QLabel{border-image:url(../Images/board.jpg);}')
        label1.setFixedWidth(700)
        label1.setFixedHeight(500)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setMaximumSize(240,240)
        btn1.setMinimumSize(240,240)

        style = '''
            #btn1{
                border-radius:10px;
                background-image:url('../Images/Sample1.png');
            }
            #btn1:Pressed{
                background-image:url('../Images/Sample3.png')
            }
        '''
        btn1.setStyleSheet(style)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(btn1)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LabelButtonBackground()
    main.show()

    sys.exit(app.exec_())