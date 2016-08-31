#! -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.qiushibaike.com/hot/')
bs = BeautifulSoup(html.text)
for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

