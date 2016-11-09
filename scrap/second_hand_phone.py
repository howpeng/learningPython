# coding:utf-8
# 列出信阳地区58网上的二手手机品牌和价格
# 页数可以修改，但目前不知道怎么自动判断总共有多少页
# 因为它是一步一步加载的，不是一次性显示的

from bs4 import BeautifulSoup
import requests
from lxml import etree

url = 'http://xy.58.com/shouji/0/'

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

def get_page_links(url):
    urls = []
    for i in range(0, 2):
        a = url + 'pn' + str(i)
        urls.append(a)
    return urls


def get_info(url):
    urls = get_page_links(url)
    m = 0
    for u in urls:
        f = requests.get(u, headers=headers)
        soup = BeautifulSoup(f.text, 'lxml')
        titles = soup.select('td.t > a')
        price = soup.select('td.t > span.pricebiao > span')
        owners = soup.select('td.tc > div > p:nth-of-type(2)')
        n = len(titles)
        m += 1
        print('Page Number:', m)
        for i in range(0, n):             # 这部分是重点，和之前用zip方法不同！
            data = {
                'title': titles[i].text,
                'price': price[i].text,
                'owner': owners[i].text
            }
            print(data)


if __name__ == '__main__':
    get_info(url)

