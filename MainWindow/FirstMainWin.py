import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()

        #设置主窗口的标题
        self.setWindowTitle('朱浩的第一个主窗口应用')

        #设置窗口的尺寸
        self.resize(400,600)

        self.status = self.statusBar()

        self.status.showMessage('只存在10秒的消息',10000)
    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./Icons/LogicAnalyser.ico'))
    main = FirstMainWin()
    main.show()
    #main.center()

    sys.exit(app.exec_())