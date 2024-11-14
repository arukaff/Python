from pymongo import MongoClient
import json

# считываем данные из JSON-файл
with open('DZ2.json', 'r') as f:
    books=json.load(f)

# подключение
client = MongoClient('mongodb://localhost:27017')
#смотрим базы
database_list = client.list_database_names()
print(database_list)

# подключение(создание) к базе данных mydb коллекции books на сервере MongoDB
db = client.mydb.books
#db.
for book_k, book_v in books.items():
  book_v['_id']=book_k
  #  добавление данных в коллекцию
  try:
        db.insert_one(book_v) 
  except:
     p=0

print('Всего книг в базе: ',db.count_documents({}))

select={'_id':0,'Описание':0 }
where={'$or':[{"Наличие":{"$gt":20}},{"Наличие":{'$lte':3}}], "Наименование":{"$regex" : "[Dd]ays | [Gg]ame"}, }
res=db.find(where,select)
for a in res:
    print (a)