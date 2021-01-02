'''

添加、修改和删除树控件中的节点

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class TreeEvent(QMainWindow):
    def __init__(self):
        super(TreeEvent, self).__init__()
        self.setWindowTitle('为树节点添加响应事件')
        self.resize(400,500)
        self.move(850,50)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(3)
        # 为树设置列标签
        self.tree.setHeaderLabels(['Key','Value','Remark'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setText(1,'0')
        root.setIcon(0,QIcon('../Images/包包/bag0.png'))
        self.tree.setColumnWidth(0,200)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'1')
        child1.setIcon(0,QIcon('../Images/包包/bag1.png'))
        child1.setCheckState(0,Qt.Unchecked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setText(1,'2')
        child2.setIcon(0,QIcon('../Images/包包/bag2.png'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'子节点2-1')
        child3.setText(1,'3')
        child3.setIcon(0,QIcon('../Images/包包/bag3.png'))

        # 展开树
        #self.tree.expandAll()

        self.tree.clicked.connect(self.onTreeClicked)

        self.setCentralWidget(self.tree)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s,value = %s' % (item.text(0),item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = TreeEvent()
    gui.show()
    app.exec_()