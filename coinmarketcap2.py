import requests
from bs4 import BeautifulSoup
import csv

# парсим название криптовалюты, цену и ссылку на страницу крипты


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('coinmarketcap2.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')

        writer.writerow([data['name'],
                        data['url'],
                        data['price']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('div', class_='cmc-table__table-wrapper-outer').find_next_sibling().find_next_sibling().\
        find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')   # метод find_all возвращает список элементов в теге td
        name = tds[1].find('a').text
        url = 'https://coinmarketcap.com' + tds[1].find('a').get('href')
        price = tds[3].find('a').text

        data = {'name': name,
                'url': url,
                'price': price}

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()