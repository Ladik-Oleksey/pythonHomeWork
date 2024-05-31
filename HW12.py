import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def fetch_weather_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Приклад парсингу (повинно бути адаптовано під конкретний сайт)
    weather_data = []
    for day in range(7):  # Парсимо дані на 7 днів вперед
        date = (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
        temperature = soup.find('div', {'class': f'temp-day-{day}'}).text
        precipitation = 'Так' if 'rain' in soup.find('div', {'class': f'precipitation-day-{day}'}).text.lower() else 'Ні'
        wind_speed = soup.find('div', {'class': f'wind-speed-day-{day}'}).text
        wind_direction = soup.find('div', {'class': f'wind-direction-day-{day}'}).text

        weather_data.append({
            'date': date,
            'temperature': temperature,
            'precipitation': precipitation,
            'wind_speed': wind_speed,
            'wind_direction': wind_direction
        })

    return weather_data

# Виклик функції
url = 'http://example.com/weather-forecast'
weather_data = fetch_weather_data(url)

import sqlite3
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_db_and_table():
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Weather (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            temperature TEXT NOT NULL,
                            precipitation TEXT NOT NULL,
                            wind_speed TEXT NOT NULL,
                            wind_direction TEXT NOT NULL
                        )''')
        conn.commit()
        logging.info('Database and table created successfully.')
    except sqlite3.Error as e:
        logging.error(f'Error creating database: {e}')
    finally:
        if conn:
            conn.close()

def insert_weather_data(weather_data):
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO Weather (date, temperature, precipitation, wind_speed, wind_direction)
                              VALUES (:date, :temperature, :precipitation, :wind_speed, :wind_direction)''', weather_data)
        conn.commit()
        logging.info('Weather data inserted successfully.')
    except sqlite3.Error as e:
        logging.error(f'Error inserting data: {e}')
    finally:
        if conn:
            conn.close()

# Створення бази даних та таблиці
create_db_and_table()

# Вставка даних
insert_weather_data(weather_data)

import sqlite3
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_db_and_table():
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Weather (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            temperature TEXT NOT NULL,
                            precipitation TEXT NOT NULL,
                            wind_speed TEXT NOT NULL,
                            wind_direction TEXT NOT NULL
                        )''')
        conn.commit()
        logging.info('Database and table created successfully.')
    except sqlite3.Error as e:
        logging.error(f'Error creating database: {e}')
    finally:
        if conn:
            conn.close()

def insert_weather_data(weather_data):
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO Weather (date, temperature, precipitation, wind_speed, wind_direction)
                              VALUES (:date, :temperature, :precipitation, :wind_speed, :wind_direction)''', weather_data)
        conn.commit()
        logging.info('Weather data inserted successfully.')
    except sqlite3.Error as e:
        logging.error(f'Error inserting data: {e}')
    finally:
        if conn:
            conn.close()

# Створення бази даних та таблиці
create_db_and_table()

# Вставка даних
insert_weather_data(weather_data)

def select_data_by_date(date):
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Weather WHERE date = ?', (date,))
        result = cursor.fetchall()
        logging.info('Data selected by date.')
        return result
    except sqlite3.Error as e:
        logging.error(f'Error selecting data: {e}')
    finally:
        if conn:
            conn.close()

def select_data_by_min_temp():
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Weather ORDER BY temperature ASC LIMIT 1')
        result = cursor.fetchall()
        logging.info('Data selected by minimum temperature.')
        return result
    except sqlite3.Error as e:
        logging.error(f'Error selecting data: {e}')
    finally:
        if conn:
            conn.close()

def select_data_by_max_temp():
    try:
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Weather ORDER BY temperature DESC LIMIT 1')
        result = cursor.fetchall()
        logging.info('Data selected by maximum temperature.')
        return result
    except sqlite3.Error as e:
        logging.error(f'Error selecting data: {e}')
    finally:
        if conn:
            conn.close()

class DateWeather:
    def __init__(self, date, temperature, precipitation, wind_speed, wind_direction):
        self.date = date
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction

def create_date_weather_objects(weather_data):
    return [DateWeather(*data) for data in weather_data]

# Використання функцій вибірки та створення об'єктів DateWeather
selected_data_by_date = select_data_by_date('2024-06-01')
date_weather_objects = create_date_weather_objects(selected_data_by_date)
