'''

树控件（QTreeWidget）的基本用法

setIconSize(QSize(width,height))

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        self.resize(400,500)
        self.move(850,50)
        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)
        # 为树设置列标签
        self.tree.setHeaderLabels(['Key','Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('../Images/包包/bag0.png'))
        self.tree.setColumnWidth(0,200)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'2323')
        child1.setIcon(0,QIcon('../Images/包包/bag1.png'))
        child1.setCheckState(0,Qt.Unchecked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('../Images/包包/bag2.png'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'子节点2-1')
        child3.setText(1,'998')
        child3.setIcon(0,QIcon('../Images/包包/bag3.png'))

        # 展开树
        self.tree.expandAll()

        self.setCentralWidget(self.tree)


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BasicTreeWidget()
    gui.show()
    app.exec_()