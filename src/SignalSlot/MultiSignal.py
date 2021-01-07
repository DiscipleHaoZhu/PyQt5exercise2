'''

为类添加多个信号

'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MultiSignal(QObject):
    # 定义一个信号
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int,str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    # 声明一个重载版本的信号，槽函数的参数可以是in和str类型，也可以只有一个str类型参数
    signal6 = pyqtSignal([int,str],[str])

    def __init__(self):
        super(MultiSignal, self).__init__()
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[str].connect(self.signalCall6Overload)
        self.signal6[int,str].connect(self.signalCall6)

        self.signal1.emit()
        self.signal2.emit(11)
        self.signal3.emit(12,'hhhhh')
        self.signal4.emit([3,'r',4,5,'de','人'])
        self.signal5.emit({'name':'朱浩','age':'33'})
        self.signal6[str].emit('test')
        self.signal6[int,str].emit(133,'testtool')


    def signalCall1(self):
        print("signal1 emit")

    def signalCall2(self,val):
        print("signal2 emit,value:",val)

    def signalCall3(self,val,text):
        print("signal3 emit,value:",val,text)

    def signalCall4(self,val):
        print("signal4 emit,value:",val)

    def signalCall5(self,val):
        print("signal5 emit,value:",val)

    def signalCall6(self,val,text):
        print("signal6 emit,value:",val,text)

    def signalCall6Overload(self, val):
        print("signal6Overload emit,value:", val)

if __name__ == '__main__':
    send = MultiSignal()
