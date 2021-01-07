'''

多线程更新UI数据(在两个线程间传递数据)

'''

from PyQt5.QtCore import QThread,pyqtSignal,QDateTime
from PyQt5.QtWidgets import QApplication,QDialog,QLineEdit
import time
import sys

class BackendThread(QThread):
    updata_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString('yyyy-MM-dd hh:mm:ss')
            self.updata_date.emit(str(currentTime))
            self.sleep(1)
            #time.sleep(1)

class ThreadUpdataUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400,100)
        self.input = QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()
    def initUI(self):
        self.backend = BackendThread()
        self.backend.updata_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdataUI()
    main.show()

    sys.exit(app.exec_())