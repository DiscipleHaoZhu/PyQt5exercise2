'''

设置单元格的文本对齐方式
setTextAlignment
Qt.AlignRight   Qt.AlignBottom

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush,QColor,QFont
from PyQt5.QtCore import Qt
import sys


class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格的文本对齐方式')
        self.resize(430,330)

        layout = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])

        newItem = QTableWidgetItem('彭程')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('女')
        newItem.setTextAlignment(Qt.AlignCenter)
        tableWidget.setItem(0,1,newItem)

        newItem = QTableWidgetItem('53')
        newItem.setTextAlignment(Qt.AlignLeft)
        tableWidget.setItem(0,2,newItem)


        self.setLayout(layout)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CellTextAlignment()
    gui.show()
    app.exec_()