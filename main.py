#! python3
# -*- coding: utf-8 -*-

'''
:FileName: main.py
:CreateBy: qinmin-006646
:CreateTime: 2018-07-23
:Description: get Don'tStave wiki information from http://zh.dontstarve.wikia.com/.
'''

#CreateTime:2018-07-23
#git@github.com:MeeQin/getDSwiki.git

import sys
from PyQt5.QtWidgets import *
from mainwindow import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle('getDSwiki')
        self.setupUi(self)
        self.treeInit()
    
    def treeInit(self):
        
        # 设置列数
        self.treeWidget.setColumnCount(2)
        # 设置头的标题
        self.treeWidget.setHeaderLabels(['Key','Value'])
        # 设置根节点
        root= QTreeWidgetItem(self.treeWidget)
        root.setText(0,'root')
        # 设置列宽
        self.treeWidget.setColumnWidth(0, 160)
        
        # 设置子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'ios')
        
        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'')      

        # 设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'android')

        self.treeWidget.addTopLevelItem(root)

        # 结点全部展开
        self.treeWidget.expandAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
