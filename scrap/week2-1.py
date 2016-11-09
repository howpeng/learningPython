# howpeng @ 2016.11.1

from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
house = client['house']
sheet_room = house['sheet_room']

url = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'

def get_more_page(url, s, e):
    urls = []
    for i in range(s, e+1):
        u = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))
        urls.append(u)
    return urls

def get_page_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    prices = soup.select("div.result_btm_con.lodgeunitname > span.result_price > i")
    titles = soup.select("div.result_btm_con.lodgeunitname > div > a > span")
    for t, p in zip(titles, prices):
        title = t.get_text()
        price = p.get_text()
        data = {
            'title': title,
            'price': int(price)
        }
        sheet_room.insert_one(data)


def print_data():
    data = sheet_room.find({'price': {'$gt': 500}})
    for i in data:
        print(i['title'], '==> ', i['price'])


if __name__ == '__main__':
    urls = get_more_page(url, 1, 10)
    for u in urls:
        get_page_info(u)
    print_data()

