# coding:utf-8
# 下载jandan上妹子图评分超过200的图

from bs4 import BeautifulSoup
import requests
import pymongo
import re

client = pymongo.MongoClient('localhost', 27017)
ooxx = client['ooxx']
sheet_200 = ooxx['sheet_200']

url = "http://jandan.net/ooxx/"

def get_page_links(url, start, end):
    urls = []
    for i in range(start, end+1):
        u = url + 'page-' + str(i)
        urls.append(u)
    return urls



def get_jpg_links(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select("div.text > p > img")
    scores_str = soup.select("div.vote")
    reg = 'OO\s\[\d{1,3}\]'
    for l, i in zip(links, scores_str):
        s = i.get_text()
        score = re.match(reg, s).group()[4:-1]
        link = l['src']
        data = {
            'link': link,
            'score': int(score)
            }
        sheet_200.insert_one(data)


def download(url):
    r = requests.get(url)
    filename = '/Users/heropeng/Desktop/xxoo/' + url[-10:-5]
    target = filename + url[-4:]
    with open(target, 'wb') as f:
        f.write(r.content)


def how_beauty(n):
    link_list = sheet_200.find({'score': {'$gt': n}})
    for link in link_list:
        download(link['link'])


if __name__ == '__main__':
    urls = get_page_links(url, 2190, 2191)
    for u in urls:
        get_jpg_links(u)
        how_beauty(10)


