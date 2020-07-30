import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool



def get_html(url):
    r = requests.get(url)
    return r.text                 # возвращает html-код страницы


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')

    tds = soup.find('div', class_='cmc-table__table-wrapper-outer').find_all('div',
                                                                               class_='cmc-table__column-name '
                                                                                      'sc-1kxikfi-0 eTVhdN')

    links = []
    for names in soup.findAll('div', class_='cmc-table__column-name sc-1kxikfi-0 eTVhdN'):
        name = names.find('a').get('href')
        link = 'https://coinmarketcap.com/' + name
        links.append(link)
    return links                         # получаем список ссылок на каждую криптовалюту

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    try:
        name = soup.find('h1').text.strip()
    except:
        name = ''

    try:
        price = soup.find('span', class_='cmc-details-panel-price__price').text.strip()
    except:
        price = ''

    data = {'name': name,
            'price': price}

    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['price']))                    # запись результатов в файл

        print(data['name'], 'parsed')




def make_all(url):
    html = get_html(url)
    data = get_page_data(html)
    write_csv(data)







def main():
    url = 'https://coinmarketcap.com/all/views/all/'

    all_links = get_all_links(get_html(url))

    #for url in all_links:


    with Pool(40) as p:
        p.map(make_all, all_links)


if __name__ == '__main__':
    main()