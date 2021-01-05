'''

装载本地Web页面

'''
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class LocalHTML(QMainWindow):

    def __init__(self):
        super(LocalHTML, self).__init__()
        self.setWindowTitle('装载本地Web页面')
        self.setGeometry(20,50,1355,730)
        url = os.getcwd() + '/test.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LocalHTML()
    main.show()
    app.exec_()