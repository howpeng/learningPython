# coding:utf-8

from bs4 import BeautifulSoup
import requests
import pymongo
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

client = pymongo.MongoClient('localhost', 27017)
gwy = client['gwy']
files = gwy['files']

# 促进民间投资文件列表
url = 'http://sousuo.gov.cn/column/40123/0.htm'

def get_more_pages(url, n):
    '''可选择要下载的页面数量'''
    urls = []
    for i in range(1, n+1):
        u = 'http://sousuo.gov.cn/column/40123/{}.htm'.format(i)
        urls.append(u)
    return urls

def get_article_link(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.select('div.list.list_1.list_2 > ul > li > h4 > a')
    for i in links:
        title = i.get_text()
        link = i['href']
        data = {
            'title': title,
            'link': link
        }
        files.insert_one(data)

def get_info(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    return r.text

def download_files(url):
    web = files.find()
    for i in web:
        target = '/Users/heropeng/Desktop/xxoo/' + i['title'] + '.html'
        content = get_info(i['link'])
        with open(target, 'w') as f:
            f.write(content)
        print(i['title'])

if  __name__ == '__main__':
    urls = get_more_pages(url, 10)
    for u in urls:
        l = get_article_link(u)
        download_files(l)


