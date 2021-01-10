'''

QSS子控件选择器

修改QComboBox下拉按钮样式

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class QSSSubControl(QWidget):
    def __init__(self):
        super(QSSSubControl, self).__init__()
        self.setWindowTitle('QSS子控件选择器')

        combo = QComboBox(self)
        combo.setObjectName('myComboBox')
        combo.addItem('Window')
        combo.addItem('Linux')
        combo.addItem('Mac OS X')

        combo.move(50,50)

        #self.setGeometry(250,200,320,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSSSubControl()
    # 更改按钮样式
    qssStyle = '''
        QComboBox#myComboBox::drop-down{
            image:url(../Images/python.jpg)
        }
    '''
    main.setStyleSheet(qssStyle)
    main.show()

    sys.exit(app.exec_())