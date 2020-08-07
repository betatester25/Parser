import requests
from bs4 import BeautifulSoup
import csv
import re

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('cmp.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')

        writer.writerow((data['name'],
                         data['url'],
                         data['price']))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('div', class_='cmc-table__table-wrapper-outer').find_next_sibling().find_next_sibling().\
        find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')  # находит все ячейке в строке таблицы

        try:
            name = tds[1].find('a').text
        except:
            name = ''
        try:
            url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        except:
            url = ''
        try:
            price = tds[3].find('a').text
        except:
            price = ''

        data = {'name': name,
                'url': url,
                'price': price}

        write_csv(data)






def main():
    url = 'https://coinmarketcap.com/'


    while True:
        get_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')

        try:
            pattern = 'Next'    # регулярное выражение
            url = 'https://coinmarketcap.com' + soup.find('div', class_='va78v0-0 bOJMMo cmc-table-listing__pagination-button-group cmc-button-group').\
                find('a', text=re.compile(pattern)).get('href')    # ищем тег а, содержащий наше регулярное выражение в тексте
        except:
            break



if __name__ == '__main__':
    main()