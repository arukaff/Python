import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent
ua=UserAgent()

# Запрос веб-страницы
url = url_1='http://books.toscrape.com'
heders={"User-Agent":ua.chrome}
session=requests.session()
books={}
while True:
  
  page = session.get(url_1,headers=heders)
  soup = BeautifulSoup(page.content, 'html.parser')
  next_page_link = soup.find('li', ('class', 'next'))
  result = soup.find_all('article', ('class','product_pod'))

  url_joined = []

  for link in result:
    try:
      l=link.find('a').get('href')
      if 'catalogue/' in l:
        url_joined.append(url+'/'+ l)
      else:
        url_joined.append(url +'/'+'catalogue/'+ l) 
    except:
      print()
  
  for u in url_joined:
    response = session.get(u)

    soup = BeautifulSoup(response.content, 'html.parser')
    # название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание

    book={}
    try:
      main=soup.find('div', ('class', 'col-sm-6 product_main'))
      book['Наименование'] = main.find('h1').text
      book['Цена'] =main.find('p', ('class', 'price_color')).text
      n=main.find('p', ('class', 'instock availability')).text
      book['Наличие'] = int(''.join(filter(lambda i: i.isdigit(), n)))
    except:
      book['Наименование'] =''
      book['Цена'] = ''
      book['Наличие'] =0

    try:
        main=soup.find('article', ('class', 'product_page'))
        book['Описание'] = main.find("p", recursive=False).text
    except:
        book['Описание'] = ''

    books['Книга '+str(len(books)+1)] = book
    

  try:
    next_link=next_page_link.find('a').get('href')
  except:  
    break
  
  if 'catalogue/' in next_link:
    url_1 = url +'/'+ next_link
  else:
    url_1 = url +'/'+'catalogue/'+ next_link

# сохранение данных в JSON-файл
with open('DZ2.json', 'w') as f:
    json.dump(books, f)