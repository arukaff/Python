from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
witcher = {
    "appid": 292030,
    "positive": 632627,
    "negative": 25245,
    "name" : "The Witcher 3: Wild Hunt",
    "developer" : "CD PROJEKT RED",
    "publisher" : "CD PROJEKT RED",
    "genre" : "RPG",
    "release_date" : "2015/05/18",
    "tags" : {
                "Open World" : 11677,
                "RPG" : 10024,
                "Story Rich" : 9219,
                "Atmospheric" : 6478,
                "Mature" : 6234,
                "Fantasy" : 6057
              }
    }
# подключение к базе данных steam на сервере MongoDB
db = client.steam
database_list = client.list_database_names()
print(database_list)

# добавление данных в коллекцию games в базе данных steam
#db.games.insert_one(witcher)

# найти все документы в коллекции games и вывести их на консоль
for a in db.games.find():
    print (a)


def find():
    query = {"developer" : "CD PROJEKT RED", "positive":{"$qt":500, "$lte":600000}} #что ищем WHERE developer=CD PROJEKT RED and positive BITWIN 500 and 6000000
    projection= {'_id':0, 'name':1} #Что выводим 0 не выводим 1 выводим SELECT name
    games = db.games.find(query, projection)
    for a in games:
        print(a)
if __name__ == '__main__':
    find()
