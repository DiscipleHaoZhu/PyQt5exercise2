'''

显示列表数据（QListView控件）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import *
import sys

class ListWidgetDemo(QMainWindow):
    def __init__(self,parent=None):
        super(ListWidgetDemo, self).__init__(parent)
        self.setWindowTitle('QListView控件演示')
        self.resize(300,270)
        self.listwidget = QListWidget()
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.addItem('item4')
        self.listwidget.addItem('item5')

        self.setCentralWidget(self.listwidget)

        self.listwidget.itemClicked.connect(self.clicked)

    def clicked(self,Index):
        QMessageBox.information(self,'QListWidget','您选择了：' + self.listwidget.item(self.listwidget.row(Index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ListWidgetDemo()
    gui.show()
    app.exec_()