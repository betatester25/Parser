from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def tel_recon(self):
        image = Image.open('tel.gif')                # создаем объект image через открытие файла
        print(image_to_string(image))


    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')    # вырезаем картинку со скриншотом
        self.tel_recon()                                         # считываем телефон с картинки



    def navigate(self):
        self.driver.get('https://www.avito.ru/rostov-na-donu/telefony/iphone_11x88776s65s54s_rassrochka_1885419987')

        button = self.driver.find_element_by_xpath("//button[@class='button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz']")
        button.click()
        sleep(3)
        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//img[@class="contacts-phone-3KtSI"]')
        location = image.location                         # возвращает словарь с координатами точки угла картинки {'x': 1234, 'y': 1234}
        size = image.size                                 # возвращает словарь с ключами {width и height}

        self.crop(location, size)










def main():
    b = Bot()





if __name__ == '__main__':
    main()