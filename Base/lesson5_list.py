# Метод extend
# Метод extend ведёт себя аналогично append, то есть добавляет элементы в конец
# списка. В качестве аргумента extend принимает последовательность, итерируется
# по ней слева направо и каждый элемент добавляет в новую ячейку списка.
a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
#my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)
# ● extend(a) — если в метод передать не коллекцию, получим ошибку TypeError.
# ● extend(b) — строка воспринимается как коллекция, в результате каждый
# символ строки помещается в новую ячейку списка.
# 9
# ● extend(c) — итерируемся по списку, c последовательно добавляя его
# элементы в список my_list
# ● extend(my_list) — удваиваем список, добавляя копию всех его элементов.


# Уточнение формата
# Существую различные способы уточнения способа вывода значения переменной.
pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
num = 2 * pi * data[1]
print(f'{num = :_}')
# После указания имени переменной в фигурных скобках ставится двоеточие —
# указатель на символы задания формата далее.
# ● :.2f — число пи выводим с точность два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и
# общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и
# только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3цифры.

#Один из способов избежать ошибки лишних (но не меньших) данных при распаковке методом split — использовать символ распаковки.
a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()
#Переменная подчёркивание благодаря звёздочке, символу упаковки, превращается в список, который заберет значения начиная с четвёртого.

