'''

JavaScript调用Python函数计算阶乘

将Python的一个对象映射到JavaScript中

将槽函数映射到JavaScript中

'''
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from factorial import *
from PyQt5.QtWebChannel import *

channel = QWebChannel()
factorial = Factorial()

class PyFactorial(QWidget):

    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python函数计算阶乘')
        self.resize(600,300)
        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.browser = QWebEngineView()
        url = os.getcwd() + './f.html'
        self.browser.load(QUrl.fromLocalFile(url))
        channel.registerObject('obj',factorial)
        self.browser.page().setWebChannel(channel)

        self.layout.addWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyFactorial()
    main.show()
    sys.exit(app.exec_())