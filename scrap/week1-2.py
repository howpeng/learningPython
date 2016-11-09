from bs4 import BeautifulSoup

url = open('/Users/heropeng/Downloads/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/index.html', 'r')

soup = BeautifulSoup(url, 'lxml')

images = soup.select('div.thumbnail > img')
titles = soup.select('div.caption > h4 > a')
prices = soup.select('div.caption > h4.pull-right')
numbers = soup.select('div.ratings > p.pull-right')
scores = soup.select('div > div.ratings > p:nth-of-type(2)')
for image, title, price, number, score in zip(images, titles, prices, numbers, scores):
    ii = image.get('src')
    tt = title.get_text()
    pp = float(price.get_text()[1:])
    cc = number.get_text()
    ss = len(score.find_all('span', "glyphicon glyphicon-star"))
    data = {
        'image': ii,
        'title': tt,
        'price': pp,
        'number': cc,
        'score': ss
    }
    print(data)
url.close()