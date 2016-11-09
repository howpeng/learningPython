#! -*-coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

url = 'http://wh.lianjia.com/ershoufang'


def get_areas(url):
    '''得到地区的url列表和名称列表，放在后面作为参数使用'''
    areas_names = []
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    areas = soup.select('div.position > dl:nth-of-type(2) > dd > div:nth-of-type(1) > div > a')
    for i in areas:
        areas_names.append(i.attrs['href'].split('/')[2])
    print(areas_names)


def get_max_page_num(url):
    '''返回一个地区的页面数量，从网页源码中找到了最大页面数字，留着后面用'''
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    num = soup.find('div', {'class': 'page-box house-lst-page-box'})
    str = num['page-data'].split(',')[0]
    n = re.search('\d+', str)
    return n.group()

get_areas(url)
get_max_page_num('http://wh.lianjia.com/ershoufang/qingshan/')





