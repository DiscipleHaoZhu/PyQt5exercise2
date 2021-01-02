'''

让控件支持拖拽动作

A->B

设置

A.setDragEnabled(True)
B.setAcceptDrops(True)

B需要两个事件
1.dragEnterEvent    将A拖到B触发
2.dropEvent         在B的区域放下A时触发


'''
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboxBox(QComboBox):
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self,event):
        print(event)
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        self.addItem(event.mimeData().text())

class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)   # 让QLineEdit控件可拖动

        combo = MyComboxBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/pyc.ico'))
    main = DrapDropDemo()
    main.show()

    sys.exit(app.exec_())