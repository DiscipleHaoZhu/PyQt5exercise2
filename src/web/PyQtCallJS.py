'''

PyQt5调用JavaScript代码

PyQt5和JavaScript交互

PyQt5 <-> JavaScript

'''
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import JSPy

class PyQtCallJS(QWidget):

    def __init__(self):
        super(PyQtCallJS, self).__init__()
        self.setWindowTitle('PyQt5调用JavaScript')
        self.setGeometry(20,50,1355,730)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.browser = QWebEngineView()

        url = os.getcwd() + './test1.html'
        self.browser.load(QUrl.fromLocalFile(url))

        self.layout.addWidget(self.browser)

        button =QPushButton('设置全名')
        button.clicked.connect(self.fullname)
        self.layout.addWidget(button)

    def js_callback(self,result):
        print(result)

    def fullname(self):
        self.value = 'hello 单点 world!'
        self.browser.page().runJavaScript('fullname("' + self.value + '");',self.js_callback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PyQtCallJS()
    main.show()
    sys.exit(app.exec_())