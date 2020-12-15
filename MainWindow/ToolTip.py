import sys
from PyQt5.QtWidgets import QDesktopWidget,QToolTip,QMainWindow,QApplication
from PyQt5.QtWidgets import QWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(900,300,500,300)
        self.setWindowTitle('设置控件提示消息')

        #添加Button
        self.button1 = QPushButton('按钮')
        self.button1.setToolTip('这是朱浩设计的按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()


    sys.exit(app.exec_())
