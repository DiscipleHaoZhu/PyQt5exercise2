'''

Override(覆盖)槽函数

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class OverriedArg(QWidget):
    def __init__(self):
        super(OverriedArg, self).__init__()
        self.setWindowTitle("Override(覆盖)槽函数")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle('zhuhaodechaunngkou')
            print('ghjklghjkf4f3fe')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = OverriedArg()
    main.show()

    sys.exit(app.exec_())
