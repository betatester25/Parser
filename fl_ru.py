import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)           # Проверка реакции сервера на запрос

def write_csv(data):
    with open('fl.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';')

        writer.writerow((data['name'],
                         data['link']))




def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    orders = soup.find_all('div', class_='b-post')



    for order in orders:
        try:
            name = order.find('h2', class_='b-post__title').find('a').text
        except:
            name = ''
        try:
            link = 'https://www.fl.ru/projects' + order.find('h2', class_='b-post__title').find('a').get('href')
        except:
            link = ''

        data = {'name': name,
                'link': link}

        write_csv(data)



def main():
    pattern = 'https://www.fl.ru/projects/?page={}&kind=5'

    for i in range(1, 4):
        url = pattern.format(str(i))
        get_data(get_html(url))



if __name__ == '__main__':
    main()
