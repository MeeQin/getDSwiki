#! python3
# -*- coding: utf-8 -*-

'''
:FileName: url.py
:CreateBy: qinmin-006646
:CreateTime: 2018-07-16
:Description: get 
'''

#CreateTime:2018-07-16
#git@github.com:MeeQin/getDSwiki.git

import os
import requests
from bs4 import BeautifulSoup

def getMenu(url):
    '''
    :FunctionName: 
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646-HomePC
    :CreateTime: 
    :Description: 
    '''

    response = requests.get(url = url)
    html = response.text

    # path = os.getcwd()
    # print(path)
    # html_path = os.path.join(path, "html", "main.html")
    # print(html_path)
    # with open(html_path, mode='rb') as html:
    #   html = open(html_path, mode='rb')

    bf = BeautifulSoup(html,'html.parser')

    gameInfo_Dict = {}
    gameInfo_L2 = []

    gameInfo = bf.find("li", class_="wds-tabs__tab")
    gameInfo_L1 = gameInfo.find('span').string
    gameInfo_Dict[gameInfo_L1] = [] # {'遊戲資料': []}

    for span in gameInfo.find('div', class_='wds-dropdown__content').find_all('span'):
        gameInfo_L2.append(span.string)
        gameInfo_Dict[gameInfo_L1].append({span.string : {}}) # {'遊戲資料': [{'遊戲功能': {}, {'角色': {}, ...}]}
    # print(gameInfo_L2) # 游戏功能... 等7个目录

    index = 0
    for div in gameInfo.find_all('div', class_='wds-dropdown-level-2__content'):
        list_L3 = []
        for a in div.find_all('a'):
            list_L3.append(a.string)
            # print(a['href'])
            gameInfo_Dict[gameInfo_L1][index][gameInfo_L2[index]][a.string] = a['href'] # {'遊戲資料': [{'遊戲功能': {'可合成': '/wiki/%E5%90%88%E6%88%90', ...}}]}
        index = index +1

    return gameInfo_Dict


if __name__ == "__main__":

    main_url = "http://zh.dontstarve.wikia.com"
    # print(getMenu(main_url))


    keyurl = '/wiki/%E5%90%88%E6%88%90'
    # getInfo(keyurl)
    url = main_url + keyurl
    response = requests.get(url = url)
    html = response.text   

    bf = BeautifulSoup(html,'html.parser')

    # getCategory(bf)
    Category_dict = {}
    Category_div = bf.find('div', class_='page-header__categories-links')
    for a in Category_div.find_all('a'):
        Category_dict[a.string] = a['href']
    print(Category_dict)


    print('End.')
    

