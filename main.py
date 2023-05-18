import sqlite3
import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.get("/coins")
def get_coins():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('SELECT * FROM coin_price')
    coins = c.fetchall()
    conn.close()

    coins_list = []
    for coin in coins:
        print(coin)
        coin_dict = {
            'id': coin[0],
            'coin': coin[1],
            'price': coin[2],
            'time': coin[3],
        }
        coins_list.append(coin_dict)

    return coins_list

