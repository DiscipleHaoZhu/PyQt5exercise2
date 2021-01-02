'''

按列排序

1.按哪一列排序
2.排序类型：升序或降序

sortItes(columnIndex,orderType)

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush,QColor,QFont
from PyQt5.QtCore import *
import sys


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('按列排序')
        self.resize(430,330)

        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)
        layout.addWidget(self.button)

        self.orderType = Qt.DescendingOrder
        self.setLayout(layout)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        newItem = QTableWidgetItem('朱浩')
        newItem.setFont(QFont('Times',18,QFont.Black))
        newItem.setForeground(QBrush(QColor(0,0,255)))
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('65')
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(1,0,newItem)

        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1,1,newItem)

        newItem = QTableWidgetItem('48')
        self.tableWidget.setItem(1,2,newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('46')
        self.tableWidget.setItem(2, 2, newItem)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(2,self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ColumnSort()
    gui.show()
    app.exec_()