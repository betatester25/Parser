import csv
from peewee import *

db = PostgresqlDatabase(database='CoinMarket', user='postgres', password='1', host='localhost')

# для корректной работы нужно чтобы в файле csv разделителем была запятая

class Coin(Model):
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db


def main():

    db.connect()
    db.create_tables([Coin])


    with open('cmp.csv') as f:
        order = ['name', 'url', 'price']                    # список колонок
        reader = csv.DictReader(f, fieldnames=order)        # создаем читателя.

        coins = list(reader)                                # создаем список


        for row in coins:
            coin = Coin(name = row['name'], url = row['url'], price = row['price'])
            coin.save()



        #with db.atomic():
            #for row in coins:
               # Coin.create(**row)   # второй способ записи данных в базу



if __name__ == '__main__':
    main()