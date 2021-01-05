'''

动态显示当前时间

QTimer
QThread

多线程：用于同时完成多个任务

'''

from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QLineEdit
from PyQt5.QtCore import QTimer,QDateTime
import sys

class ShowTime(QWidget):
    def __init__(self):
        super(ShowTime, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.resize(300,200)

        self.label = QLabel('显示当前时间')
        self.timeEdit = QLineEdit()
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label,0,0,)
        layout.addWidget(self.timeEdit, 0, 1,1,2)

        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.setLayout(layout)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

    def showTime(self):
        time = QDateTime.currentDateTime()

        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowTime()
    main.show()
    app.exec_()