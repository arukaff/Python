# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки

import json
from pathlib import Path
import csv

def condert(f:Path):
    data={}
    with open(f,'r') as file:
        for line in file:
            name, number = line.strip().split('|')
            data[name.strip().capitalize()] = float(number)

    with open(f.stem + '.json','w', encoding='utf-8') as file_ex:
        json.dump(data,file_ex, indent=4, ensure_ascii=False)

condert(Path('random.txt'))

# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

def set_users(u_f: Path) ->None:
    uniq_id= set()
    if not u_f.is_file():
        data={str(i):{} for i in range(1,7+1)}
    else:
        with open(u_f,'r',encoding='utf-8') as file:
            data=json.load(file)
            for dict in data.values():
                uniq_id.update(dict)
    
    while True:
        name = input('Enter name:')
        user_id = input('Enter id:')
        level = input('Enter level 1 - 7:')
        if user_id not in uniq_id:
            data[level].update({user_id: name})
            uniq_id.add(user_id)
            with open(u_f,'w',encoding='utf-8') as file:
                json.dump(data,file,indent=4, ensure_ascii=False)


#set_users(Path('new.json'))

# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

def json_to_csv(file: Path)->None:
    with open(file,'r',encoding='utf-8') as f:
        data=json.load(f)
    rows =[]
    for level, dict_level in data.items():
        for user_id, name in dict_level.items():
            rows.append({'level':int(level),'id': int(user_id), 'name':name})
        
    with open(f'{file.stem}.csv', 'w', newline='',encoding='utf-8') as f:
        csv_write = csv.DictWriter(f,fieldnames=['level','id','name'])
        csv_write.writeheader()
        csv_write.writerows(rows)

json_to_csv(Path('new.json'))

# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import pickle


def json_2_picle(path:Path):
    for obj in path.iterdir():
        if obj.is_file() and obj.suffix =='.json':
            with open(obj,'r',encoding='utf-8') as f_r:
                data=json.load(f_r)
            with open(f'{obj.stem}.picle','wb') as f_w:
                pickle.dump(data,f_w)

json_2_picle(Path.cwd())