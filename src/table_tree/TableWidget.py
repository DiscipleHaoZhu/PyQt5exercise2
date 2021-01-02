'''

扩展的表格控件（QTableWidget）

是QTabelView的子类

QTableWidget的每个Cell（单元格）是一个QTableWidgetItem

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableView表格视图控件演示')
        self.resize(400,230)
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem = QTableWidgetItem('小米')
        tablewidget.setItem(0,0,nameItem)

        ageItem = QTableWidgetItem('24')
        tablewidget.setItem(0,1,ageItem)

        jgItem = QTableWidgetItem('安徽')
        tablewidget.setItem(0,2,jgItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 自动调整列和行
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        # 隐藏表头
        #tablewidget.horizontalHeader().setVisible(False)
        #tablewidget.verticalHeader().setVisible(False)

        tablewidget.setVerticalHeaderLabels(['a','b'])

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TableWidgetDemo()
    gui.show()
    app.exec_()