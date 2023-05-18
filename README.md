<div align="center">

# Crypto Price Tracker

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

**Crypto Price Tracker** This application was created for fun and you could just use CoinGecko API directly. **Crypto Price Tracker** uses CoinGecko API for fetching real-time prices, stores data in SQLite, and exposes an API endpoint to fetch the historical price data. It also provides a Python script to visualize this data using Matplotlib.

---

## :sparkles: Features

- **Real-time** cryptocurrency price tracking
- Data stored in **SQLite**
- **API endpoint** for fetching historical data
- **Visualization** of price data over time

---

## :clipboard: Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- Libraries: FastAPI, Uvicorn, Requests, Matplotlib, SQLite

> These requirements can be installed by running `pip install -r requirements.txt`

---

## :file_folder: Project Structure

Here's a brief intro to the main files in this repository:

- `main.py`: Contains the FastAPI server and the endpoint that fetches data from the SQLite database.
- `plot.py`: Fetches data from the FastAPI server and plots the cryptocurrency price over time.
- `fetch_price.py`: Fetches the current price of the cryptocurrency from the CoinGecko API and inserts it into the SQLite database.

---

## :rocket: Getting Started

#### 1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

#### 2. Run the script that fetches the current price and inserts it into the database:

```bash
python fetch_price.py
```

#### 3. Run the script that fetches data from the FastAPI server and plots it:

```bash
python plot.py
```

You should see a matplotlib window pop up displaying the plot of the cryptocurrency price over time.


:handshake: Contributing:

Contributions, issues, and feature requests are welcome!

:memo: License:

This project is MIT licensed.