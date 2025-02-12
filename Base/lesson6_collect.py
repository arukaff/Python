# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
ls=[1,2,3,4,5,1,4,5,3,2,1,5]
print(list(set(ls)))
ls.sort()
print(ls)
for i in ls:
    for _ in range(ls.count(i)-1):
        ls.remove(i)
print(ls)

# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data=(42,73,3.14,'Hello',None,True,'Text',100500.2,False)
result={}
for item in data:
    item_type=type(item)
    if item_type not in result:
        result[item_type]=[item]
    else:
        result[item_type].append(item)
print(result)

# variant2
res={}
for item in data:
    item_type=type(item)
    if item_type not in res:
        res[item_type]=[el for el in data if type(el)==item_type]
print(res)

# variant3
r={}
for item in data:
    key = r.setdefault(type(item),[]).append(item)
print(r)

# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды
ls=[1,2,3,4,5,1,4,5,3,2,1,5]
print(ls)
ls_new=[el for el in ls if ls.count(el)!=2]
print(ls_new)
COUNT=2
for item in set(ls): #проходим по уникальным элементам только
    if ls.count(item)==COUNT: #усли таких значений два
        for _ in range(COUNT):
            ls.remove(item) # удаляем два раза
print(ls)

# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.
ls=[1,2,3,4,5,1,4,5,3,2,1,5]
ls_new=[]
for i, item in enumerate(ls,1):
    if item % 2:
        ls_new.append(i)
ls_new=[n for n,el in enumerate(ls,1) if el%2]
print(ls_new)

# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
ls = sorted(list(input('Введите строку текста: ').split()))
w_len=0
for w in ls:
    if w_len<len(w):
        w_len=len(w)
for ns, item in enumerate(ls,1):
     print(f'Строка №{ns:<2} {item:>{w_len}}')

# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях

str = input('Введите строку текста: ')
res={}
for ch in set(str):
    res[ch]= str.count(ch)
print (res)
#2
res1={}
for ch in str:
    if ch not in res1:
        res1[ch]=1
    else:
        res1[ch]+=1
print (res1)
#3
res2={}
for ch in str:
    res2[ch]= res2.get(ch,0)+1
print (res2)

# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
hike ={
    'Азат': ( 'спички', 'спальник', 'дрова', 'топор'),
    'Марат':( 'спальник', 'спички', 'вода', 'еда'),
    'Андрей':( 'вода', 'спички', 'косметика'),
}
all_ =set()
# all_.update(*hike.values) так тоже работает полный список вещей
# print(all_)
# print(*hike.values) 
for values in hike.values():
    all_.update(values)
print(f'полный список вещей: {all_=}')
un={}
for master_friend, masret_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend!=slave_friend:
            if master_friend not in un:
                un[master_friend] = set(masret_things)-set(slave_things)
            else:
                un[master_friend] -= set(slave_things)
print(f'уникальный список вещей: {un=}')

dubl_=set(all_)
un_=set()
un_.update(*un.values())
print(un_)# уникальные вещи которые есть у всех вместе
dubl_-=un_
print(dubl_) #  вещи каторые есть у каждого - дубликаты
for friends, things in hike.items():
    n_thi=dubl_-set(things)
    if n_thi:
        print(f'У {friends} отсутствуют {n_thi} ')