#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import random
import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
wh_shouji = client['wu_shouji']
url_list = wh_shouji['url_list']
item_info = wh_shouji['item_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
'Connection': 'keep-alive'}

proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
]

proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}


def get_links(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    titles = soup.find_all('a', attrs={'class': 't'})
    prices = soup.select('span.pricebiao > span.price')
    for l, p in zip(titles, prices):
        title = l.get_text()
        price = p.get_text() + '元'
        data = {
            'title': title,
            'price': price
        }
        item_info.insert_one(data)




def get_more_pages(channel):
    urls = []
    for page in range(1, 100):
        url = 'http://wh.58.com/{}/pn{}/'.format(channel, page)
        urls.append(url)
    return urls

if __name__ == '__main__':
    urls = get_more_pages('shouji')
    for u in urls:
        get_links(u)
