'''

装载Gif动画
QMovie

'''

from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPainter,QPixmap,QMovie
import sys

class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()
        self.label = QLabel('',self)
        self.setFixedSize(320,240)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie('../Images/gif/001.gif')
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoadingGif()
    main.show()

    sys.exit(app.exec_())


