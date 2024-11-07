import requests
import json
from keys import Foursquare_key


url = "https://api.foursquare.com/v3/places/search"
# Определение параметров для запроса API
category = {'1':'4bf58dd8d48988d181941735','2':'63be6904847c3692a84b9bb6','3':'4bf58dd8d48988d163941735','4':'4d4b7105d754a06374d81259'}
city = input("Введите название города: ")
c= input("Введите интересующую вас категорию заведения: 1 - Музеи, 2 - кофейни, 3- парки, 4- рестораны: ")
if c not in category.keys():
    c=3
    print("Хорошо Парки")

params = {
    "near": city,
    "sort": 'RATING',
    "categories": category.get(c)
}

headers = {
    "Accept": "application/json",
    "Authorization": Foursquare_key
}

# Отправка запроса API и получение ответа
response = requests.get(url, params=params,headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print(f'Успешный запрос заведений в городе {city}')
    j_data = response.json()
    for place in j_data.get('results'):
        print("Название:", place.get("name"))
        print("Адрес:", place.get("location").get("address"))
        print("Рейтинг:", place.get("rating"))
        print("\n")
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)
