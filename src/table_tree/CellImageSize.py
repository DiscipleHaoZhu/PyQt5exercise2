'''

改变单元格中图片的尺寸

setIconSize(QSize(width,height))

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('改变单元格中图片的尺寸')
        self.resize(1000,900)

        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setIconSize(QSize(300,200))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        # 设置列的宽度和图片的宽度相同
        for i in range(3):
            self.tableWidget.setColumnWidth(i,300)

        # 设置行的高度和图片的高度相同
        for i in range(5):
            self.tableWidget.setRowHeight(i,300)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.tableWidget.setHorizontalHeaderLabels(['图片1','图片2','图片3'])

        for k in range(15):
            i = k / 3
            j = k % 3
            item = QTableWidgetItem()
            item.setIcon(QIcon('../Images/包包/bag%d.png' % k))
            self.tableWidget.setItem(i,j,item)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = CellImageSize()
    gui.show()
    app.exec_()