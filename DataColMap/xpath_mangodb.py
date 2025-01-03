import requests
from lxml import html
from pymongo import MongoClient

def insert_to_db(list_movies):
    if len(list_movies)>0:
        client = MongoClient("mongodb://localhost:27017")
        db = client["imdb_movies"]
        collection = db["top_movies"]
        collection.insert_many(list_movies)
        client.close()

all_movies = []

resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm', headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
})
print(resp.status_code)
tree = html.fromstring(html=resp.content)

#movies = tree.xpath("//table[@data-caller-name='chart-moviemeter']/tbody/tr")

# def get_titlemeter(list_element):
#     try:
#         return(list_element[0].split()[-1])
#     except:
#         return "no change"

# def get_position_change(list_element):
#     try:
#         return(int(list_element[0].strip()[:-1]))
#     except:
#         return 0
movies = tree.xpath("//li[@class='ipc-metadata-list-summary-item sc-4929eaf6-0 DLYcv cli-parent']")
for movie in movies:
    # m = {
    #     'name' : movie.xpath(".//td[contains(@class, 'titleColumn')]/a/text()")[0],
    #     'release_year' : int(movie.xpath(".//td[contains(@class, 'titleColumn')]/span/text()")[0][1:-1]),
    #     'position' : int(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/text()")[0].split()[0]),
    #     'titlemeter' : get_titlemeter(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/span/@class")),
    #     'position_change' : get_position_change(movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/text()[2]"))
    # }
    #all_movies.append(m)
    try:
        m = {
        'name': movie.xpath(".//div[contains(@class, 'cli-title')]/a/h3/text()")[0],
        'release_year': movie.xpath(".//div[contains(@class, 'cli-title-metadata')]/span/text()")[0],
        'position': movie.xpath(".//div[contains(@class, 'meter-const-ranking')]/text()")[0],
        'titlemeter': movie.xpath(".//div[contains(@class, 'meter-const-ranking')]/span/svg[contains(@class, 'sc-db6887cf-0')]/@class")[0],
        'position_change': movie.xpath(".//div[contains(@class, 'meter-const-ranking')]/span/text()")[0]
        }
    except IndexError:
    # Обрабатываем случаи, когда какой-то элемент не был найден
        continue
    all_movies.append(m)

insert_to_db(all_movies)
print(all_movies) 
print(len(all_movies))