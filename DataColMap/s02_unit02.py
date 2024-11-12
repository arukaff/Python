import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua=UserAgent()

# Запрос веб-страницы
url = 'https://www.boxofficemojo.com'
#url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
heders={"User-Agent":ua.chrome}# ua.random ставим если не используем сесия, а постоянно перезапрашиваем реквест - будет подставлятся разные браузеры
params={"ref_":"bo_nb_hm_tab"}
# requests.get постоянно перезапрашивает данные, что создает опасную активность, лучше открывать сессию и вней делать запросы
session=requests.session()

response = session.get(url+"/intl",params=params, headers=heders)

# Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Хотим забрать со страницы таблицу, по этому берем все теги tr
rows = soup.find_all('tr')
#создаем список заголовков
headers = [header.text.strip() for header in rows[0].find_all('th')]
#создаем список строк
films=[]
#проходим циклом по строкам с третьей строки(исключаем заголовки) 
for row in rows[2:]:
    film={} # свой словарь под каждую строку  
    cells = row.find_all('td')
    if cells:
        #film['Area']= [row.find('a',{'class':'a-link-normal'}).getText(),url + row.find('a',{'class':'a-link-normal'}).get('href') ]# первый столбец сохраняем и ссылку и текст в список есть еще вариант вместо find('a')  findCildren()
        film[headers[0]] = [cells[0].find('a').text, url + cells[0].find('a').get('href')]
        film[headers[1]] = [cells[1].find('a').text, url + cells[1].find('a').get('href')]
        film[headers[2]] = int(cells[2].text)
        try:
            film[headers[3]] = [cells[3].find('a').text, url + cells[3].find('a').get('href')]
        except:
            film[headers[3]] =None
        try:
            film[headers[4]] = [cells[4].find('a').text.strip(), url + cells[4].find('a').get('href')]
        except:
            film[headers[4]] =None
        try:
            film[headers[5]] = int(cells[5].text.replace('$', '').replace(',', ''))
        except:
            film[headers[5]] =0    
        
        
    films.append(film)

import pandas as pd
df = pd.DataFrame(films)
print(df)
