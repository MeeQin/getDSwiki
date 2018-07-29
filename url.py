#! python3
# -*- coding: utf-8 -*-

'''
:FileName: url.py
:CreateBy: qinmin-006646
:CreateTime: 2018-07-16
:Description: get Don'tStave wiki information from http://zh.dontstarve.wikia.com/.
'''

#CreateTime:2018-07-16
#git@github.com:MeeQin/getDSwiki.git

import os
import re
import json
import requests
from bs4 import BeautifulSoup
from langconv import *


def cht_to_chs(line):
    # 转换繁体到简体
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

def chs_to_cht(line):
    # 转换简体到繁体
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

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

    bf = BeautifulSoup(html,'html.parser')

    gameInfo_Dict = {}
    gameInfo_Menu = {}
    gameInfo_L2 = []

    gameInfo = bf.find("li", class_="wds-tabs__tab")
    gameInfo_L1 = cht_to_chs(gameInfo.find('span').string)
    gameInfo_Dict[gameInfo_L1] = [] # {'遊戲資料': []}

    for span in gameInfo.find('div', class_='wds-dropdown__content').find_all('span'):
        gameInfo_L2.append(cht_to_chs(span.string))
        gameInfo_Dict[gameInfo_L1].append({cht_to_chs(span.string) : {}})
        # {'遊戲資料': [{'遊戲功能': {}, {'角色': {}, ...}]}

    index = 0
    for div in gameInfo.find_all('div', class_='wds-dropdown-level-2__content'):
        list_L3 = []
        for a in div.find_all('a'):
            list_L3.append(cht_to_chs(a.string))
            # print(a['href'])
            gameInfo_Dict[gameInfo_L1][index][gameInfo_L2[index]][cht_to_chs(a.string)] = a['href']
            # {'遊戲資料': [{'遊戲功能': {'可合成': '/wiki/%E5%90%88%E6%88%90', ...}}]}
            gameInfo_Menu[cht_to_chs(a.string)] = a['href']
        index = index +1

    path = os.getcwd()
    tree_path = os.path.join(path, "resource", "tree.json")
    menu_path = os.path.join(path, "resource", "menu.json")
    with open(tree_path, mode='w', encoding='utf-8') as f:
        data = json.dumps(gameInfo_Dict,sort_keys=True,indent =4,separators=(',', ': '),ensure_ascii=False )
        f.write(data)
    with open(menu_path, mode='w', encoding='utf-8') as f:
        data = json.dumps(gameInfo_Menu,sort_keys=True,indent =4,separators=(',', ': '),ensure_ascii=False )
        f.write(data)
    return gameInfo_Dict

def getArticle(keyword, keyurl):
    '''
    :FunctionName: getArticle
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646-HomePC
    :CreateTime: 
    :Description: 
    '''
    url = main_url + keyurl
    response = requests.get(url = url)
    html = response.text   

    bf = BeautifulSoup(html,'html.parser')

    # # getCategory(bf)
    # Category_dict = {}
    # Category_div = bf.find('div', class_='page-header__categories-links')
    # for a in Category_div.find_all('a'):
    #     if 'href' in a :
    #         Category_dict[a.string] = a['href']
    # print(Category_dict)

    # get article
    # <article id="WikiaMainContent" class="WikiaMainContent">
    article = bf.find_all('article', class_='WikiaMainContent')
    path = os.getcwd()
    filename = keyword + '.html'
    article_path = os.path.join(path, "html", "wiki", "article", filename)
    with open(article_path, mode='w',encoding='utf-8') as article_f:
        # Category_s = str(Category_div)
        # Category_s = Category_s[1:]
        # Category_s = Category_s[:-1]   
        # Category_lines = Category_s.splitlines()
        # for line in Category_lines:
        #     line_chs = cht_to_chs(line)
        #     article_f.writelines(line_chs)

        article_s = str(article)
        article_s = article_s[1:]
        article_s = article_s[:-1]
        article_lines = article_s.splitlines()
        for line in article_lines:
            line_chs = cht_to_chs(line)
            article_f.writelines(line_chs)

def getImgFile(bf):
    '''
    :FunctionName: 
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646-HomePC
    :CreateTime: 
    :Description: 
    '''
    path = os.getcwd()
    img_path = os.path.join(path, 'html')

    for img in bf.find_all('img'):
        #print(img.attrs)
        if 'data-src' in img.attrs.keys():
            data_src = img['data-src']
            data_image_name = img['data-image-name']
            m = re.search('dont-starve-game/(.*)/revision',data_src)
            if m:
                img_name = m.groups()[0]
                print(m.groups()[0])
        elif 'src' in img.attrs.keys():
            data_src = img['src']
            data_image_name = img['data-image-name']
            m = re.search('dont-starve-game/(.*)/revision',data_src)
            if m:
                img_name = m.groups()[0]
                print(m.groups()[0])  
        
        img_name = img_name.replace('/', '\\')
        response = requests.get(url = data_src)
        html = response.content            
        img_data_path = os.path.join(img_path, img_name)
        [dirpath, imgname] = os.path.split(img_data_path)
        if not os.path.exists(img_data_path):
            if not os.path.isdir(dirpath):  
                os.makedirs(dirpath)
            with open(img_data_path, mode='wb') as f:
                f.write(html)          

def replaceImgSrc(bf):
    '''
    :FunctionName: 
    :param: 
    :ReturnType: 
    :CreateBy: qinmin-006646-HomePC
    :CreateTime: 
    :Description: 
    '''
    for img in bf.find_all('img'):
        print('ok')

if __name__ == "__main__":

    main_url = "http://zh.dontstarve.wikia.com"
    # getMenu(main_url)

    # path = os.getcwd()
    # menu_path = os.path.join(path, "resource", "menu.json")
    # with open(menu_path, mode='r', encoding='utf-8') as f:
    #     data = f.read()
    #     menu = json.loads(data)
    #     print(menu)
    
    # for keyword in menu:
    #     print(keyword)
    #     keyurl = menu[keyword]
    #     getArticle(keyword,keyurl)
    path = os.getcwd()
    test_path = "C:\\getDSwiki\\getDSwiki\\html\\test-可合成.html"
    with open(test_path, mode='r', encoding='utf-8') as f:
        html = f.read()
        bf = BeautifulSoup(html,'html.parser')
        getImgFile(bf)

    keyurl = '/wiki/%E5%90%88%E6%88%90'
    keyword = '可合成'
    # getInfo(keyurl)

    

    print('End.')


    

    

