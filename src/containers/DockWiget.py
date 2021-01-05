'''

停靠控件（QDockWidget）

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)

        self.setWindowTitle('停靠控件（QDockWidget）')

        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable',self)
        self.lisWidget = QListWidget()
        self.lisWidget.addItem('item1')
        self.lisWidget.addItem('item2')
        self.lisWidget.addItem('item3')

        self.items.setWidget(self.lisWidget)

        self.setCentralWidget(QLineEdit())

        #self.items.setFloating(True)

        self.addDockWidget(Qt.LeftDockWidgetArea,self.items)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DockDemo()
    gui.show()
    app.exec_()