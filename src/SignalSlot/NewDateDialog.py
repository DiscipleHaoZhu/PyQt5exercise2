from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class NewDateDialog(QDialog):
    Signal_OneParameter = pyqtSignal(str)
    def __init__(self,parent=None):
        super(NewDateDialog, self).__init__(parent)
        self.setWindowTitle('子窗口：用来发送信号')

        layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setText('前者发送内置信号\n后者发送自定义信号')
        self.datetime_inner = QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.label)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)
        self.setLayout(layout)

        # 使用两个button（ok和cancel）分别连接accept()和reject()槽函数
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

    def emit_signal(self):
        date_str = self.datetime_emit.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)
