# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
wuhan = client['wuhan']
ershoufang = wuhan['ershoufang']

url = 'http://wh.lianjia.com/ershoufang/'

def get_more_pages(url,start, end):
    urls = []
    for i in range(start, end+1):
        u = url + 'pg' + str(i)
        urls.append(u)
    return urls


def get_info(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    titles = soup.select('div.info.clear > div.title > a')
    infos = soup.select('div.info.clear > div.address > div')
    position_infos = soup.select('div.info.clear > div.flood > div')
    total_prices = soup.select('div.info.clear > div.priceInfo > div.totalPrice > span')
    unit_prices = soup.select('div.info.clear > div.priceInfo > div.unitPrice > span')
    for t, i, p , t, u in zip(titles, infos, position_infos, total_prices, unit_prices):
        title = t.get_text()
        info = i.get_text()
        position_info = p.get_text()
        floor = position_info.split()[0]
        formate = position_info.split()[1]
        address = position_info.split()[-1]
        total_price = t.get_text()
        unit_price = u.get_text()
        data = {
             'title': title,
             'info': info,
             'floor': floor,
             'build_date': formate,
             'address': address,
             'total_price': total_price,
             'unit_price': unit_price
         }
        ershoufang.insert_one(data)

if __name__ == '__main__':
    urls = get_more_pages(url, 1, 100)
    for u in urls:
        get_info(u)