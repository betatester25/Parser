from selenium import webdriver


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')


    def navigate(self):
        self.driver.get('https://www.avito.ru/rostov-na-donu/telefony/iphone_11x88776s65s54s_rassrochka_1885419987')

        button = self.driver.find_element_by_xpath("//button[@class='button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz']")
        button.click()
        self.take_screenshot()










def main():
    b = Bot()





if __name__ == '__main__':
    main()