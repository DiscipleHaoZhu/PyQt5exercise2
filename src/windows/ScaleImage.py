'''

播放图片

'''

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtGui import QPainter,QPixmap,QMovie,QImage
import sys

class ScaleImage(QWidget):
    def __init__(self):
        super(ScaleImage, self).__init__()
        self.setWindowTitle('图片大小缩放例子')
        filename = '../Images/floor tile1.jpg'
        img = QImage(filename)
        label1 = QLabel(self)
        label1.setFixedWidth(900)
        label1.setFixedHeight(900)
       # result = img.scaled(label1.width(),label1.height())
        result = img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label1)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScaleImage()
    main.show()

    sys.exit(app.exec_())


