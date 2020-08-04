import requests
from bs4 import BeautifulSoup
import csv


# со страницы с плагинами получаем информацию о названии каждого плагина, количество отзывов и ссылки

def get_html(url):
    r = requests.get(url)
    return r.text


def refind(s):
    # 1,790 total ratings
    r = s.split(' ')[0]  # разделяем выражение на элементы и оставляем только элемент с числом рейтинга
    result = r.replace(',', '')  # заменяем запятые на ничего
    return result


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['rating']))  # записываем полученные данные в файл


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text  # название плагина
        url = plugin.find('h3').find('a').get('href')  # ссылка на плагин
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refind(r)  # получаем только цифры рейтинга

        data = {'name': name,
                'url': url,
                'rating': rating}

        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
