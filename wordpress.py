import requests
from bs4 import BeautifulSoup


# https://wordpress.org/

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', id='home-welcome').find('header').find('h1')
    return title.text


def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
