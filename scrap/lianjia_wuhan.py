# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import re

client = pymongo.MongoClient('localhost', 27017)
wuhan = client['wuhan']
ershoufang = wuhan['ershoufang']

r_url = 'http://wh.lianjia.com/ershoufang/'

def get_areas(url):
    '''得到地区的url列表和名称列表，放在后面作为参数使用'''
    areas_names = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    areas = soup.select('div.position > dl:nth-of-type(2) > dd > div:nth-of-type(1) > div > a')
    for i in areas:
        areas_names.append(i.attrs['href'].split('/')[2])
    return areas_names


def get_max_page_num(url):
    '''返回一个地区的页面数量，从网页源码中找到了最大页面数字，留着后面用'''
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    num = soup.find('div', {'class': 'page-box house-lst-page-box'})
    str = num['page-data'].split(',')[0]
    n = re.search('\d+', str)
    return n.group()


def get_more_pages(url, n):
    urls = []
    for i in range(1, int(n)+1):
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
    areas = get_areas(r_url)
    for a in areas:
        urls = get_more_pages(url=r_url+a, n=get_max_page_num(r_url+a))
        for u in urls:
            get_info(u)

