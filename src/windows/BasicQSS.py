'''

QSSjic
QSS(QT Style Sheets)
Qt样式表

用于设置控件的样式

例如叠层样式表：CSS

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class BasicQSS(QWidget):
    def __init__(self):
        super(BasicQSS, self).__init__()
        self.setWindowTitle('QSS样式')
        self.resize(300,400)

        vbox = QVBoxLayout()
        btn1 =QPushButton(self)
        btn1.setText('按钮1')
        btn2 =QPushButton(self)
        btn2.setText('按钮2')

        btn3 =QPushButton(self)
        btn3.setText('按钮3')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicQSS()
    # 选择器
    qssStyle = '''
        QPushButton{
            background-color:red
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())