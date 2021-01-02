'''

设置单元格字体和颜色

'''

from PyQt5.QtWidgets import QWidget,QTableWidget,QHBoxLayout,QApplication,QTableWidgetItem
from PyQt5.QtGui import QBrush,QColor,QFont
import sys


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格字体和颜色')
        self.resize(600,800)

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
        tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('惊奇队长')
        newItem.setForeground(QBrush(QColor(255,255,0)))
        newItem.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CellFontAndColor()
    gui.show()
    app.exec_()