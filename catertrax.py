import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.3.100 '
                                'Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def write_csv(data):
    with open('catertrax.csv', 'a') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order, delimiter=';')
        writer.writerow(data)


def get_page_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article', class_='testimonial-post')
    print(ts)
    #return ts      # непустой или пустой список отзывов


def get_page_data(ts):

    for i in ts:
        try:
            since = i.find('p', class_='traxer-sincev').text.strip()
        except:
            since = ''
        try:
            author = i.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {'author': author, 'since': since}
        write_csv(data)



def main():


    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page))

        articles = get_page_articles(get_html(url))   # или пустой список или непустой

        if articles:
            get_page_data(articles)
            page += 1
        else:
            break



if __name__ == '__main__':
    main()