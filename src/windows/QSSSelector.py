'''

使用QSS选择器设置控件样式

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class QSSSelector(QWidget):
    def __init__(self):
        super(QSSSelector, self).__init__()
        self.setWindowTitle('使用QSS选择器设置控件样式')
        self.resize(300,400)

        vbox = QVBoxLayout()
        btn1 =QPushButton(self)
        btn1.setText('按钮1')
        btn2 =QPushButton(self)
        btn2.setProperty('name','btn2')
        btn2.setText('按钮2')

        btn3 =QPushButton(self)
        btn3.setText('按钮3')
        btn3.setProperty('name', 'btn3')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSSSelector()
    # 选择器
    qssStyle = '''
        QPushButton[name="btn2"]{
            background-color:red;
            color:yellow;
            height:120;
            font-size:80px;
        }
        QPushButton[name="btn3"]{
            background-color:blue;
            color:green;
            height:120;
            font-size:80px;
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())