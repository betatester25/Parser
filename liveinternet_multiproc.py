import requests
import csv
from multiprocessing import Pool

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def write_csv(data):
    with open('sites_list.csv', 'a', encoding='utf8') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';')
        writer.writerow(data)


def get_page_data(text):
        data = text.strip().split('\n')[1:]    # убрали лишние пробелы и табуляцию (strip), разбили строку
                                                   # в список по критерию переноса строки и удалили первый элем.

        for row in data:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}


            write_csv(data)

def make_all(url):
    text = get_html(url)
    get_page_data(text)


def main():
    # 6163 страницы
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(0, 6164)]

    with Pool(20) as p:                   # количество процессов
        p.map(make_all, urls)



if __name__ == '__main__':
    main()