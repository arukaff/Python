from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import csv

driver = webdriver.Chrome()
driver.get("https://www.imdb.com/search/title/")
try:
    # открываем выпадающее поле rating
    button_according=driver.find_element(By.XPATH, "//label[@data-testid='accordion-item-ratingsAccordion']")
    button_according.click()

    # вводим текст
    input_rating = driver.find_element(By.XPATH, "//input[@data-testid='imdbratings-start']") 
    input_rating.send_keys("9")

    # открываем выпадающее поле keywords
    button_according=driver.find_element(By.XPATH, "//label[@data-testid='accordion-item-keywordsAccordion']")
    button_according.click()

    # вводим текст
    input_rating = driver.find_element(By.XPATH, "//input[@data-testid='test-keywords-refiner']") 
    input_rating.send_keys("anime") 

    # нажимаем кнопку обновить
    button_res=driver.find_element(By.XPATH, "//button[@data-testid='adv-search-get-results']")
    button_res.click()

    print(driver.current_url)
    response = requests.get(driver.current_url, headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})
    # Закрываем драйвер
    driver.quit()

    # Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []
    try:
        rows = soup.find_all('div', {'class': 'ipc-metadata-list-summary-item__tc'})
        
        for row in rows:
            row_data=[]
            try: 
                title = row.find('h3', {'class': 'ipc-title__text'}).text.strip()
                row_data.append(title) 
                rening = row.find('span', {'class': 'ipc-rating-star--rating'}).text.strip()
                row_data.append(rening)
                descript = row.find('div', {'class': 'ipc-html-content-inner-div'}).text.strip()
                row_data.append(descript)
                data.append(row_data)
            except:
                print('Ошибка при парсинге фильма')
    except:
        print('Ошибка при парсинге данных')

    with open('SeleniumDZ.csv', 'w',encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(['title','rening','descript'])
        write.writerows(data)
except:
    print('Ошибка при формировании запроса к сайту')



