# Импорт необходимых библиотек
import requests
from lxml import html
import csv


# Определение целевого URL
url = "https://www.timeanddate.com/weather"

# Отправка HTTP GET запроса на целевой URL с пользовательским заголовком User-Agent
response = requests.get(url, headers = {
   'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
tree = html.fromstring(response.content)
# Использование выражения XPath для выбора всех строк таблицы 
table = tree.xpath("//table[@class='zebra fw tb-theme']")#table[@class='zebra fw tb-theme']
table_rows=table[0].xpath(".//tr")

data = []
for row in table_rows:
    city = row.xpath(".//td/a/text()")
    temp = row.xpath(".//td[@class='rbi']/text()")
    tds = zip(city, temp)
    for td in tds:
          t=''.join(x for x in td[1] if x.isdigit())
          data.append([td[0],t])
    
with open('weather.csv', 'w',encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(['city','temp'])
        write.writerows(data)
print(data)