'''

创建透明窗口

'''

from PyQt5.Qt import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMainWindow()
    main.setWindowTitle('窗口的透明度设置')
    main.resize(400,300)
    # 0到1，0表示完全透明，1表示不透明
    main.setWindowOpacity(0.3)

    button = QPushButton('我的按钮',main)

    main.show()

    sys.exit(app.exec_())


