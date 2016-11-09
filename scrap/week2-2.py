from bs4 import BeautifulSoup
import requests
import pymongo
from

from
url = 'http://bj.58.com/shoujihao/'



def get_pages(url, s, e):
    urls = []
    for i in range(s, e+1):
        u = url + 'pn' + i
        urls.append(u)
    return urls


def get_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    title = soup.select('#jingzhun > a.t')[0].text
    link = soup.select('#jingzhun > a.t')[0]['href']
    print(title,link)

if __name__ == '__main__':
    get_info(url)
