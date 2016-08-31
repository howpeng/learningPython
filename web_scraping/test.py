#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup

download_url = 'http://movie.douban.com/top250'

def download_page(url):
    data = requests.get(url)
    return data.text

def main():
    print(download_page(download_url))

def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detail.find('span', attrs={'class':'title'}).getText()
        print(movie_name)


if __name__ == '__main__':
    main()

