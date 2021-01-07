'''

自定义信号
pyqtSignal()

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    # 定义发送3个参数的信号
    sendmsg3 = pyqtSignal(str,int,int)

    def run(self):
        self.sendmsg.emit('Hello wold!')

    def run1(self):
        self.sendmsg3.emit('hello',34,78)

class MySlot(QObject):
    def get(self,ms):
        print('信息' + ms)

    def get1(self,mss,a,b):
        print(mss)
        print(a+b)

if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()

    send.sendmsg.connect(slot.get)
    send.sendmsg3.connect(slot.get1)
    send.run()
    # 解除信号槽绑定
    send.sendmsg.disconnect(slot.get)

    send.run()
    send.run1()