'''

设置单元格尺寸

'''

from PyQt5.QtWidgets import QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem
from PyQt5.QtGui import QBrush,QColor,QFont
import sys


class CellSize(QWidget):
    def __init__(self):
        super(CellSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格尺寸')
        self.resize(600,400)

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)
        self.setLayout(layout)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        newItem = QTableWidgetItem('雷神')
        newItem.setFont(QFont('Times',28,QFont.Black))
        newItem.setForeground(QBrush(QColor(0,0,255)))
        tableWidget.setRowHeight(0,60)
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('分工会尽快发过火惊人带我覅就奇队长')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setColumnWidth(1,300)
        tableWidget.setItem(0,1,newItem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CellSize()
    gui.show()
    app.exec_()