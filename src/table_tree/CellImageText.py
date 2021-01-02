'''

在单元格实现图文混排的效果

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class CellSize(QWidget):
    def __init__(self):
        super(CellSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格实现图文混排的效果')
        self.resize(600,400)

        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）','显示图片'])

        newItem = QTableWidgetItem('李宁')
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('100')
        self.tableWidget.setItem(0,2,newItem)

        # 设置单元格同时显示图片和文本
        newItem = QTableWidgetItem(QIcon('../Images/board.jpg'),'电路板')
        self.tableWidget.setItem(0,3,newItem)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CellSize()
    gui.show()
    app.exec_()