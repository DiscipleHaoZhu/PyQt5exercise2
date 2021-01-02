'''

合并单元格
从row,col所在单元格开始向下向右计算合并的单元格个数
setSpan(row,col,要合并的行数，要合并的列数)

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush,QColor,QFont
from PyQt5.QtCore import Qt
import sys


class Span(QWidget):
    def __init__(self):
        super(Span, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('合并单元格')
        self.resize(430,330)

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        newItem = QTableWidgetItem('彭程')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0,0,newItem)
        tableWidget.setSpan(0,0,3,1)

        newItem = QTableWidgetItem('女')
        newItem.setTextAlignment(Qt.AlignCenter)
        tableWidget.setItem(0,1,newItem)
        tableWidget.setSpan(2,1,2,2)

        newItem = QTableWidgetItem('53')
        newItem.setTextAlignment(Qt.AlignLeft)
        tableWidget.setItem(0,2,newItem)
        tableWidget.setSpan(0,2,4,1)


        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Span()
    gui.show()
    app.exec_()