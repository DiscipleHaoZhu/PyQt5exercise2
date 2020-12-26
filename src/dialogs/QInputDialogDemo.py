'''

对话框：QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')
        self.resize(300,200)

        layout = QFormLayout()
        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.get_Item)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.button1,self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.get_Text)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2,self.lineEdit2)

        self.button3 = QPushButton('获取数字')
        self.button3.clicked.connect(self.get_Int)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3,self.lineEdit3)

        self.setLayout(layout)
    def get_Item(self):
        items = ('C','C++','Ruby','Python','Java')
        item,ok = QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)

    def get_Text(self):
        text, ok = QInputDialog.getText(self, '输入文本框', '输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)
    def get_Int(self):
        num, ok = QInputDialog.getInt(self, '输入整数', '输入数字')
        if ok and num:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/LogicAnalyser.ico'))
    main = QInputDialogDemo()
    main.show()

    sys.exit(app.exec_())