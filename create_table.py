import sqlite3
import requests
import time
import datetime

CRYPTO_CURRENCY = "bitcoin"
FIAT_CURRENCY = "usd"

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS coin_price(id integer primary key, coin text, price real, time timestamp default current_timestamp)')
    conn.commit()

def insert_coin_data(coin, price):
    now = datetime.datetime.now().replace(microsecond=0)
    c.execute('INSERT INTO coin_price(coin, price, time) VALUES (?, ?, ?)', (coin, price, now))
    conn.commit()

def get_current_price():
    base_url = "https://api.coingecko.com/api/v3"
    endpoint = f"/simple/price?ids={CRYPTO_CURRENCY}&vs_currencies={FIAT_CURRENCY}"

    response = requests.get(base_url + endpoint)

    if response.status_code == 200:
        current_price_data = response.json()
        current_price = current_price_data[CRYPTO_CURRENCY][FIAT_CURRENCY]
        print(f"Coin: {CRYPTO_CURRENCY} Current price: {current_price} Time: {datetime.datetime.now().replace(microsecond=0)}")
        insert_coin_data(CRYPTO_CURRENCY, current_price)

if __name__ == '__main__':
    create_table()
    while True:
        get_current_price()
        time.sleep(6)
