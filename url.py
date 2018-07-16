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
    html = open(html_path, mode='rb')
    bf = BeautifulSoup(html,'html.parser')
    

