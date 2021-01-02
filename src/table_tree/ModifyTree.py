'''

添加、修改和删除树控件中的节点

'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.setWindowTitle('添加、修改和删除树控件中的节点')
        self.resize(450,500)
        self.move(850,50)

        operatorLayout = QHBoxLayout()
        addBtn = QPushButton('添加节点')
        updataBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updataBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updataBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)


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
        self.tree.expandAll()

        self.tree.clicked.connect(self.onTreeClicked)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key = %s,value = %s' % (item.text(0),item.text(1)))


    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0,'修改节点')
        item.setText(1,'值已经被修改')

    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ModifyTree()
    gui.show()
    app.exec_()