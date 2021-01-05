'''

日历控件
QCalendarWidget

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()
    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))

        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showData)
        self.label =QLabel(self)
        data = self.cal.selectedDate()
        self.label.setText(data.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)

        self.resize(400,350)
        self.setWindowTitle('日历演示')

    def showData(self,data):
        #self.label.setText((data.toString('yyyy-MM-dd dddd')))
        self.label.setText((self.cal.selectedDate().toString('yyyy-MM-dd dddd')))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/pyc.ico'))
    main = MyCalendar()
    main.show()

    sys.exit(app.exec_())