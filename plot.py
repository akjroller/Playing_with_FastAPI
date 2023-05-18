import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Make a GET request to your API
response = requests.get('http://localhost:8000/coins')

# The data from the API is returned as JSON, so you can call .json() to convert it to Python data structures
coins = response.json()

# Prepare data for plotting
times = [datetime.strptime(coin['time'], '%Y-%m-%d %H:%M:%S') for coin in coins]
prices = [coin['price'] for coin in coins]

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(times, prices)

# Format the x-axis to properly display times
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()

# Add title and labels
plt.title('Bitcoin price over time')
plt.xlabel('Time')
plt.ylabel('Price')

# Display the plot
plt.show()
