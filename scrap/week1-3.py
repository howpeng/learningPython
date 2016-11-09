from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.xiaozhu.com'

def get_inner_links(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.find_all('a', attrs={'class': 'resule_img_a'})
    return links


def get_page_links(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.find('div', attrs={'class':'pagination_v2 pb0_vou'}).find_all('a')
    return links

def get_info(url):
    links = get_inner_links(url)
    for link in links:
        time.sleep(1)
        web_data = requests.get(link.get('href'))  #此处应注意link是一个a标签，而不是纯连接，所以要用.get('href')
        soup = BeautifulSoup(web_data.text, 'lxml')
        title = soup.select('div.con_l > div.pho_info > h4 > em')
        address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
        rent = soup.select('#pricePart > div.day_l > span')
        pic = soup.select('#curBigImage')
        own_pic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
        own_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')


        for tt, aa, rr, pp, op, on in zip(title, address, rent, pic, own_pic, own_name):
            t = tt.get_text()
            a = aa.get_text()
            r = rr.get_text()
            p = pp.get('src')
            oi = op.get('src')
            oe = on.get_text()
            data = {'title': t,
                    'address': a,
                    'rent': r,
                    'picture': p,
                    'own_picture': oi,
                    'own_name': oe}

            print(data)

if __name__ == '__main__':
    done = []
    page_link = get_page_links(url)
    for i in page_link:
        if i not in done:
            get_info(i.get('href'))
            done.append(i)
        elif i in done:
            continue
