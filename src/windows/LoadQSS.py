'''

装载QSS文件

'''

from PyQt5.QtWidgets import *
from CommonHelper import CommonHelper
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('装载QSS文件')
        self.resize(500,350)
        btn = QPushButton()
        btn.setText('装载QSS文件')
        btn.setToolTip('提示文本')

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        self.setLayout(vbox)

        btn.clicked.connect(self.onClick)

        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(vbox)


    def onClick(self):
        styleFile = './style.qss'
        qssStyle = CommonHelper.readQSS(styleFile)
        main.setStyleSheet(qssStyle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())


