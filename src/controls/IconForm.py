import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon

'''
Windows和Linux下
窗口和QApplication的setWindowIcon方法均可设置窗口图标和应用图标

MAC下
窗口图标无法显示
仅QApplication的setWindowIcon方法可以设置应用图标
'''


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        # 设置窗口标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口图标
        # self.setWindowIcon(QIcon('./Icons/Cpp.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('../Icons/LogicAnalyser.ico'))
    main = IconForm()
    main.show()
    # main.center()

    sys.exit(app.exec_())
