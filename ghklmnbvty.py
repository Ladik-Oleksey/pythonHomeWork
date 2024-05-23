import sqlite3


conn = sqlite3.connect('weather.db')

c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS weather

            (date_time TEXT, temperature REAL)''')


conn.commit()

conn.close()

import requests


url = 'https://ua.sinoptik.ua/погода-львів'

response = requests.get(url)


if response.status_code == 200:

   html = response.content

else:

   print('Не вдалося отримати сторінку')

from bs4 import BeautifulSoup


soup = BeautifulSoup(html, 'html.parser')

today_weather = soup.find('div', {'class': 'weatherToday'}).find('div', {'class': 'temperature'}).text

today_temperature = int(today_weather.split('°')[0])


print(f"Температура сьогодні: {today_temperature}°C")

import datetime

import sqlite3


# Отримання температури і збереження її до бази даних

temperature = today_temperature

date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


conn = sqlite3.connect('weather.db')

c = conn.cursor()


c.execute("INSERT INTO weather VALUES (?, ?)", (date_time, temperature))


conn.commit()

conn.close()