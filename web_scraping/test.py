#! -*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import time
import re

html = requests.get('http://zz.58.com/yihelu/ershoufang/h1k1/?PGTID=0d30000c-0015-73e2-a861-5682b22109ad&ClickID=2')
bs = BeautifulSoup(html.text)
t = bs.findAll('tr', {'sort': re.compile('.*')})
for i in t:
    print(i.text)


