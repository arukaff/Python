# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def sort_print(s):
    ls = sorted(s.split())
    w_len=len(max(ls,key=len))
    for ns, item in enumerate(ls,1):
        print(f'Строка №{ns:<2} {item:>{w_len}}')


#sort_print(input('Введите строку текста: '))

# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию
def print_cod(string):
    # s_cod=[]
    # for s in set(string):
    #     s_cod.append(ord(s))
    # return sorted(s_cod,reverse=True)
    return sorted([ord(s) for s in set(string)],reverse=True)

#print(print_cod(input('Введите строку текста: ')))


# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.
def create_dict(str):
    n1, n2 = map(int,str.split())
    res={}
    for n in range(min(n1,n2), max(n1,n2)+1):
        res[chr(n)]=n
        #res.setdefault(chr(n),n)
    return res


print(create_dict('1 10'))

# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def buble_sort(data):
    n=len(data)
    for i in range(n):
        fl=True
        for j in range(0,n-i-1):
            if data[j]>data[j+1]:
                data[j], data[j+1]=data[j+1],data[j]
                fl=False
        if fl:
            return data
        

ls=[45,65,73,21]
print(buble_sort(ls))


# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

def award(names,sala,bonus):
    res={}
    for name, salary, award in zip(names, sala, bonus):
        res[name]=salary*award
    print(res)
    return res


names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary* award:.2f}')
award(names, salaries, awards)

# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
def sum_list(numbers,n1,n2):
    size=len(numbers)
    min_i,max_i= sorted([n1,n2])
    min_i=min_i if min_i>0 else 0
    max_i=max_i if max_i<size else size
    return sum(numbers[min_i:max_i])

s=[73,42,7,3,5,2,11,111,511,1,-400]
print(sum_list(s,3,8))


# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
def bal(f):
    return all(map(lambda n: sum(n)>=0,f.values()))


data={
    "Hjuf":[42,-73,12],
    "rjgsnf":[45,-100,22],
    "Hdjcns":[-500,123,45],
}
print(bal(data))

# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def remove_s()->None:
    dic_vars=globals()
    for key in dic_vars.copy:
        if key.endswith('s') and key !='s':
            dic_vars[key[:-1]]= dic_vars[key]
            dic_vars[key]=None
    print(dic_vars)


datas =[]