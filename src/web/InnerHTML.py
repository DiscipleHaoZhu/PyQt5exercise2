'''

显示嵌入Web页面

'''
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class InnerHTML(QMainWindow):

    def __init__(self):
        super(InnerHTML, self).__init__()
        self.setWindowTitle('显示嵌入Web页面')
        self.setGeometry(20,50,1355,730)

        self.browser = QWebEngineView()
        self.browser.setHtml('''<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>测试页面</title>
            </head>
            <body>
            <h1>Hello PyQt5 朱浩</h1>
            <h2>Hello PyQt5</h2>
            <h3>Hello PyQt5</h3>
            <h4>Hello PyQt5</h4>
            <h5>Hello PyQt5</h5>
            </body>
            </html>''')

        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = InnerHTML()
    main.show()
    app.exec_()