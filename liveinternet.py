import requests
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open('liveinternet.csv', 'a', encoding='utf8') as f:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';')
        writer.writerow(data)


def main():

    for i in range(0, 6260):  # всего 6259 сайтов, но range генерирует ДО последнего числа

        url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
        responce = get_html(url)          # получили ответ сервера в виде текста
        data = responce.strip().split('\n')[1:]    # убрали лишние пробелы и табуляцию (strip), разбили строку
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




if __name__ == '__main__':
    main()