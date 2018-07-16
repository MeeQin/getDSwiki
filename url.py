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


if __name__ == "__main__":
    # main_url = "http://zh.dontstarve.wikia.com/"
    # response = requests.get(url = main_url)
    # html = response.text

    path = os.getcwd()
    # print(path)
    html_path = os.path.join(path, "html", "main.html")
    # print(html_path)
    with open(html_path, mode='rb') as html:
        html = open(html_path, mode='rb')
        bf = BeautifulSoup(html,'html.parser')

        gameInfo_L1 = []
        gameInfo_L2 = []
        gameInfo_L3 = []
        gameInfo_list = [gameInfo_L1, gameInfo_L2, gameInfo_L3]

        gameInfo = bf.find("li", class_="wds-tabs__tab")
        print(gameInfo.find('span').string)
        gameInfo_L1.append(gameInfo.find('span').string)
        print(gameInfo_L1) # 游戏资料
        for span in gameInfo.find('div', class_='wds-dropdown__content').find_all('span'):
            print(span.string)
            gameInfo_L2.append(span.string)
        print(gameInfo_L2) # 游戏功能... 等7个目录

        for div in gameInfo.find_all('div', class_='wds-dropdown-level-2__content'):
            list_L3 = []
            for a in div.find_all('a'):
                list_L3.append(a.string)
            gameInfo_L3.append(list_L3)
        print(gameInfo_L3)

    print('End.')
    

