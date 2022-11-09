# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)

import requests
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
full_data = response.json()
names_craft = full_data['people']
list_spacemen = []
for count in range(len(names_craft)):
    list_spacemen.append((names_craft[count]['name']))
print(list_spacemen)

# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# результатом буде приблизно такий результат
# {"coord":{"lon":30.7326,"lat":46.4775},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations","main":{"temp":13.94,"feels_like":12.8,"temp_min":13.94,"temp_max":13.94,"pressure":1021,"humidity":54,"sea_level":1021,"grnd_level":1015},"visibility":10000,"wind":{"speed":4.58,"deg":314,"gust":8.16},"clouds":{"all":73},"dt":1664909335,"sys":{"country":"UA","sunrise":1664855942,"sunset":1664897549},"timezone":10800,"id":698740,"name":"Odesa","cod":200}
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране

city = 'kiev'
weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
response_weather = requests.get(weather_url)
full_data_weather = response_weather.json()
temperature = full_data_weather['main']['temp']
wind_speed = full_data_weather['wind']['speed']
print(f'temperature in {city} is {temperature} and speed of wind in {city}  is {wind_speed}')