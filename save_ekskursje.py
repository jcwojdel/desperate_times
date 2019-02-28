import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://wo.blox.pl{}'
START_URL = '/2019/02/Now-that-it-s-all-over.html'


def get_one_page(url):
    return requests.get(BASE_URL.format(url)).text


def get_previous_url(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find(id='BlogWpisPoprzedniLewy').a['href']


def save_page(url, page):
    with open(url.replace('/', '_'), 'w') as f:
       f.write(page)


url = START_URL
while url:
    print(url)
    page = get_one_page(url)
    save_page(url, page)
    url = get_previous_url(page)
