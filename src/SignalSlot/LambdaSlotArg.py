'''

使用Lambda表达式为槽函数传递参数

Lambda表达式：匿名函数，也就是没有名字的函数

fun = lambda :print('hello zhuhao')

fun()

fun1 = lambda x,y:print("x+y=",x+y)
fun1(33,59)

'''

from PyQt5.QtWidgets import *
import sys

class LamdaSlotArg(QMainWindow):
    def __init__(self):
        super(LamdaSlotArg, self).__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")

        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        ddf = -253.5
        button1.clicked.connect(lambda:self.onButtonClick(10,ddf))
        button2.clicked.connect(lambda: self.onButtonClick(50, -2))
        button1.clicked.connect(lambda:QMessageBox.information(self,'jieguo', '单击了button1'))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onButtonClick(self,m,n):
        print('m + n = ',m+n)
        QMessageBox.information(self,'结果',str(m+n))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LamdaSlotArg()
    main.show()

    sys.exit(app.exec_())
