'''

显示列表数据（QListView控件）

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import *
import sys

class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.setWindowTitle('QListView控件演示')
        self.resize(300,270)

        layout = QVBoxLayout()
        listview = QListView()
        listModel = QStringListModel()
        self.list = ['列表项1','列表项2','列表项3']

        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self,item):
        QMessageBox.information(self,'QListView','您选择了：' + self.list[item.row()])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ListViewDemo()
    gui.show()
    app.exec_()