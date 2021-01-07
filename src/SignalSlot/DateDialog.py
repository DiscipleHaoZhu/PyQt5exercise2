from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateDialog(QDialog):
    def __init__(self,parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle('DateDialog')

        layout = QVBoxLayout()
        self.date_time = QDateTimeEdit(self)
        self.date_time.setCalendarPopup(True)
        self.date_time.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.date_time)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

    def dateTimedd(self):
        return self.date_time.dateTime()

    @staticmethod
    def getDateTime(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec()
        date = dialog.dateTimedd()
        return (date.date(),date.time(),result == QDialog.Accepted)