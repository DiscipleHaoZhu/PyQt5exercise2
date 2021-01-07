'''

多窗口交互（1）：不使用信号和槽

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from DateDialog import DateDialog

class MultiWindow1(QWidget):
    def __init__(self):
        super(MultiWindow1, self).__init__()
        self.setWindowTitle('多窗口交互（1）：不使用信号和槽')
        self.resize(300,100)

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.btn1_clicked)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.btn2_clicked)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

        self.setLayout(gridLayout)

    def btn1_clicked(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.dateTimedd()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def btn2_clicked(self):
        date,time,result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('点击取消按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindow1()
    main.show()

    sys.exit(app.exec_())