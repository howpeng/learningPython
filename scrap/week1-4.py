from bs4 import BeautifulSoup
from lxml import etree
import requests

url = 'http://jandan.net/ooxx'
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


def main(url):
    r = requests.get(url, headers=headers)
    selector = etree.HTML(r.text)
    imgs = selector.xpath("//div[@class='text']/p/img/@src")
    for i in imgs:
        download(i)



def download(url):
    r = requests.get(url, headers=headers)
    filename = url[40:-10]
    target = '{}.jpg'.format(filename)
    with open(target, 'wb') as fs:
        fs.write(r.content)

if __name__ == '__main__':
    main(url)