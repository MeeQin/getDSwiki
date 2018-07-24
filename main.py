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

import os
import sys
import json
from PyQt5.QtWidgets import *
from mainwindow import *


def getTreeJson():
    '''
    :FunctionName: getTreeJson
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646
    :CreateTime: 2018-07-23
    :Description: 
    '''
    path = os.getcwd()
    tree_path = os.path.join(path, "resource", "tree.json")
    with open(tree_path, mode='r', encoding='utf-8') as f:   
        data = json.load(f)
        return data

def getMenuJson():
    '''
    :FunctionName: getMenuJson
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646
    :CreateTime: 2018-07-23
    :Description: 
    '''
    path = os.getcwd()
    menu_path = os.path.join(path, "resource", "menu.json")
    with open(menu_path, mode='r', encoding='utf-8') as f:   
        data = json.load(f)
        return data    

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.treeInit()
    
    def treeInit(self):
        
        # 设置列数
        self.treeWidget.setColumnCount(1)
        # 设置头的标题
        self.treeWidget.setHeaderLabels(['关键字'])
        # 隐藏标题
        self.treeWidget.setHeaderHidden(True)

        # 从json文件获取dict
        data = getTreeJson()
        for key1 in data:
            # 设置根节点
            root= QTreeWidgetItem(self.treeWidget)
            root.setText(0,key1)
            list1 = data[key1]
            for index in range(0,len(list1)-1):
                # type(data[key1]) = list
                for key2 in list1[index]:
                    # data[key1][index][key2] = dict
                    child1 = QTreeWidgetItem(root)
                    child1.setText(0,key2)       
                    for key3 in list1[index][key2]:
                        child2 = QTreeWidgetItem(child1)
                        child2.setText(0,key3)                    
        self.treeWidget.addTopLevelItem(root)
        # 节点全部展开
        self.treeWidget.expandAll()

        self.treeWidget.itemClicked.connect(self.treeOnClick)

    def treeOnClick(self, item, column):
        '''
        :FunctionName: 
        :param: 
        :ReturnType: 
        :CreateBy: qinmin-006646
        :CreateTime: 
        :Description: 
        '''
        print(item.text(0))
        item_text = item.text(0)
        filename = item_text + ".html"
        path = os.getcwd()
        print(path)  
        article_path = os.path.join(path, "html", "wiki", "article", filename)
        print(article_path)    
        with open(article_path, mode='r', encoding='utf-8') as article:
            data = article.read()
            self.textBrowser.insertPlainText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

