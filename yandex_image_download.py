import requests
import os

#url = 'https://img5.goodfon.ru/wallpaper/nbig/c/87/brooklyn-bridge-park-brooklyn-bridge-new-york-city-bruklinsk.jpg'

urls = ['https://cdn.pixabay.com/photo/2020/05/04/13/30/outdoors-5129182__340.jpg',
        'https://i1.wallbox.ru/wallpapers/main/201251/nyu-jork-f52e235.jpg',
        'https://habrastorage.org/r/w1560/webt/1y/qs/wu/1yqswuuknqxuwcnerqenogyqwby.jpeg',
        'https://icdn.lenta.ru/images/2020/08/01/15/20200801155007057/pic_ca397036b24a11d1add3bee3163baac5.jpg']


def get_file(url):
    r = requests.get(url, stream=True)
    return r                                     # получение файла по частям

def get_name(url):
    name = url.split('/')[-1]                    # присвоение имени файлу с помощью разделения url по слэшу
    folder = name.split('.')[0]                  # присвоение имени папки по урлу

    if not os.path.exists(folder):
        os.makedirs(folder)                      # если папки с таким именем еще нет, то создать папку

    path = os.path.abspath(folder)

    return path + '/' + name

def save_image(name, file_object):
    with open(name, 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)



#def get_image(url):
   # r = requests.get(url, stream=True)

   # with open('1.jpg', 'bw') as f:
    #    for chunk in r.iter_content(8192):
    #        f.write(chunk)







def main():

    for url in urls:
        save_image(get_name(url), get_file(url))




  #  get_image(url)


if __name__ == '__main__':
    main()
