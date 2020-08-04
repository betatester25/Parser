import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text  # возвращает html-код страницы


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages clearfix').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)  # получаем общее количество страниц


def write_csv(data):
    with open('avito.csv', 'a', encoding='utf8') as f:
        writer = csv.writer(f)

        writer.writerow((data['title'],
                         data['price'],
                         data['address'],
                         data['url']))  # записываем результаты в файл


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    ads = soup.find('div', class_='snippet-list js-catalog_serp').find_all('div', class_='item_table')

    for ad in ads:
        # название, цена, место, url

        try:
            title = ad.find('div', class_='snippet-title-row').find('h3').text
        except:
            title = ''

        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='snippet-title-row').find('h3').find('a').get('href')
        except:
            url = ''

        try:
            price = ad.find('div', class_='snippet-price-row').text.strip()
        except:
            price = ''

        try:
            address = ad.find('span', class_='item-address-georeferences-item__content').text
        except:
            address = ''  # Получаем ссылку, название, цену и район для каждого товара

        data = {'title': title,
                'price': price,
                'address': address,
                'url': url}
        write_csv(data)


def main():
    url = 'https://www.avito.ru/rostov-na-donu/bytovaya_elektronika?p=2'
    base_url = 'https://www.avito.ru/rostov-na-donu/bytovaya_elektronika?'  # неизменяемая часть адреса
    page_part = 'p='  # указание на номер страницы

    total_pages = get_total_pages((get_html(url)))

    for i in range(1, 3):
        url_gen = base_url + page_part + str(i)  # получаем url каждой страницы
        print(url_gen)
        html = get_html(url_gen)  # получаем html-код каждой страницы
        get_page_data(html)  # считываем со страницы нужные данные


if __name__ == '__main__':
    main()
