# coding:utf-8
from bs4 import BeautifulSoup
from lxml import etree
import requests


url = 'http://xy.58.com/ershoufang/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
           'Cookie': 'userid360_xml=F40AA491DFB94859FF7F348203C1A6B6; time_create=1479906067402; f=n; id58=c5/ns1gOBeF0yh4ZAxaUAg==; ipcity=xy%7C%u4FE1%u9633%7C0; als=0; myfeet_tooltip=end; f=n; 58home=xy; bj58_id58s="dzhCYm1KNkNHdmxVODg3NQ=="; sessionid=fd61b3f1-9352-4538-a353-1d786424ff9d; FTAPI_BLOCK_SLOT=FUCKIE; FTAPI_Source=xy.58.com/; bj58_new_session=0; bj58_init_refer="http://xy.58.com/"; bj58_new_uv=1; city=xy; 58tj_uuid=5c8bf401-8a6e-49ca-ada4-96b4af54d6d4; new_session=0; new_uv=1; utm_source=; spm=; init_refer=; FTAPI_ASD=1; FTAPI_PVC=1017820-2-iuojvdhs; FTAPI_ST=1017820-2-iupi64yb'}


def get_links(url):
    web_data = requests.get(url, headers=headers)
    selector = etree.HTML(web_data.text)
    links = selector.xpath("//p[@class='bthead']/a/@href")
    return links


def get_more_page(url):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    selector = etree.HTML(web_data.text)
    links = selector.xpath("//*[@id='house-area']/a/@href")
    return links



def get_info(url):
    web_data = requests.get(url, headers=headers)
    selector = etree.HTML(web_data.text)
    title = selector.xpath("//p[@class='bthead']/a/text()")
    address = selector.xpath("//div[@class='qj-listleft']/text()")
    price = selector.xpath("//b[@class='pri']/text()")
    style = selector.xpath("//span[@class='showroom']/text()")
    for t, a, p, s in zip(title, address, price, style):
        tt = t.strip()
        aa = a.strip()
        pp = p.strip()
        ss = s.strip()
        data = {
            'title': tt,
            'address': aa,
            'price': pp+'万元',
            'style': ss
        }
        stttt = data['title'] + data['style'] + data['price']
        f = open('tt.txt', 'w')
        f.write(stttt+'\n')
        f.close()



if __name__ == '__main__':
    get_info(url)