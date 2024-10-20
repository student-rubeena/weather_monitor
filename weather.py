import requests
import time

API_KEY = 'your_api_key'  # Replace with your actual API key
CITY_IDS = {
    'Delhi': '1264527',
    'Mumbai': '1275339',
    'Chennai': '1264528',
    'Bangalore': '1275771',
    'Kolkata': '1264525',
    'Hyderabad': '1264520'
}

def fetch_weather_data():
    for city, city_id in CITY_IDS.items():
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric')
        if response.status_code == 200:
            data = response.json()
            print(f"Weather in {city}: {data['main']['temp']}°C, Condition: {data['weather'][0]['main']}")
        else:
            print(f"Failed to retrieve data for {city}.")
    time.sleep(300)  # Wait for 5 minutes

if __name__ == "_main_":
    while True:
        fetch_weather_data()
        import sqlite3
from datetime import datetime

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS weather_summary (
        date TEXT,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT
    )
''')

weather_data = {}

def store_weather_summary(date, temp, condition):
    if date not in weather_data:
        weather_data[date] = {'temps': [], 'conditions': []}
    weather_data[date]['temps'].append(temp)
    weather_data[date]['conditions'].append(condition)

def calculate_daily_summary():
    for date, data in weather_data.items():
        avg_temp = sum(data['temps']) / len(data['temps'])
        max_temp = max(data['temps'])
        min_temp = min(data['temps'])
        dominant_condition = max(set(data['conditions']), key=data['conditions'].count)
        c.execute("INSERT INTO weather_summary VALUES (?, ?, ?, ?, ?)",
                  (date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()
    temperature_threshold = 35  # Example threshold

def check_alerts(current_temp):
    if current_temp > temperature_threshold:
        print("Alert! Temperature exceeds threshold."
              def fetch_weather_data():
    for city, city_id in CITY_IDS.items():
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}&units=metric')
        if response.status_code == 200:
            data = response.json()
            current_temp = data['main']['temp']
            condition = data['weather'][0]['main']
            date = datetime.now().date().isoformat()

            store_weather_summary(date, current_temp, condition)
            check_alerts(current_temp)
            print(f"Weather in {city}: {current_temp}°C, Condition: {condition}")
        else:
            print(f"Failed to retrieve data for {city}.")
    time.sleep(300)  # Wait for 5 minutes
    import matplotlib.pyplot as plt

def plot_weather_data():
    dates = []
    avg_temps = []
    for row in c.execute('SELECT * FROM weather_summary'):
        dates.append(row[0])
        avg_temps.append(row[1])
    plt.plot(dates, avg_temps, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperature')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()'end=')