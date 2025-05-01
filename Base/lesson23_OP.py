# 1. Класс как функция
# При желании можно заставить класс, а точнее его экземпляры вести себя как
# функции. После имени экземпляра указываются круглые скобки с параметрами для
# вызова и экземпляр возвращает ответ. Разберём как это работает.

from collections import defaultdict
class Storage:
    def __init__(self):
        self.storage = defaultdict(list)
    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'
    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'
s = Storage()
print(s(42))
print(s(72))
print(s('Hello world!'))
print(s(0))
print(s)

# 2. Создаём итераторы
# Список list можно передать в цикл for in для перебора его элементов, итерации.
# Также итерироваться по списку можно в генераторных выражениях. А можно
# передать список функции для итерации, например функции all(). У итерируемых
# объектов много способов использования. Можно ли создать итерируемый объект
# самому? Да. Если экземпляр класса должен итерироваться, необходимо
# реализовать пару дандер методов.
# Создадим класс экземпляр которого будет выдавать числа Фибоначчи в диапазоне
# начиная с числа больше или равного start и заканчивая числом меньше stop.

class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1
    def __iter__(self):
        return self
    def __next__(self):
        while self.first < self.stop:
            self.first, self.second = self.second, self.first + self.second
            if self.start <= self.first < self.stop:
                return self.first
        raise StopIteration
fib = Fibonacci(20, 100)
for num in fib:
    print(num)

# 3. Создаём менеджер контекста with
# Менеджер контекста with запускает два дандер метода. Один в момент вызова
# менеджера, а второй в момент выхода из внутреннего блока кода. Знакомая нам
# функция open() поддерживает работу с менеджером контекста. При вызове
# менеджера функция возвращает файловый дескриптор. А при выходе из него
# закрывает файл. Подобный функционал можно реализовать для любого объекта,
# где нужны одинаковые действия в начале и в конце. Рассмотрим пример работы с
# базой данных sqlite.


import sqlite3

class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None
    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")

# 4. Декоратор @property
# На прошлой лекции мы работали с классом треугольник и пометили его свойства
# защищёнными, добавив символ подчёркивания в начале имени. Но что если доступ
# к свойству нужен. Хотя бы на чтение. Для этого отлично подойдёт функция
# декоратор property(). Рассмотрим на более простом и коротком примере.


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = 0
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > self._age:
            self._age = value
        else:
            raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
    @age.deleter
    def age(self):
        self._age = 0
    
user = User('Стивен', 'Спилберг')
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
#user.full_name = 'Стивен Хокинг' # AttributeError: can't set attribute 'full_name'
user.last_name = 'Хокинг'
print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')

user.age = 75
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошёл один год.')
user.age = 76
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
#user.age = 25 # ValueError: Новый возраст должен быть больше текущего: 76
del user.age
print(f'Меня зовут {user.full_name} и мне {user.age} лет.')


# 5. Дескрипторы
# Дескриптор - это атрибут объекта со “связанным поведением”, то есть такой
# атрибут, при доступе к которому его поведение переопределяется методом
# протокола дескриптора. Эти методы __get__, __set__ и __delete__. Если хотя бы
# один из этих методов определен в объекте , то можно сказать что этот метод
# дескриптор.
# Звучит немного сложно. Так и есть. Дескрипторы не нужны для простых классов. Их
# польза проявляется при метапрограммировании, создании фреймворков.
# Посмотрите на то как в Django создаются модели для работы с базой данных.
# Пример взят из официальной документации

class Range:
    def __init__(self, min_value: int = None, max_value: int =  None):
        self.min_value = min_value
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя  удалять')
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым   числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше   {self.max_value}')
class Student:
    age = Range(3, 103)
    grade = Range(1, 11 + 1)
    office = Range(3, 42 + 1)
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office
    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'

if __name__ == '__main__':
    std_one = Student('Архимед', 12, 4, 29)
    #std_other = Student('Аристотель', 2406, 5, 17) # ValueError: Значение 2406 должно быть меньше 103
print(f'{std_one = }')
std_one.age = 15
print(f'{std_one = }')
#std_one.grade = 11.0 # TypeError: Значение 11.0 должно быть целым числом
#std_one.office = 73 # ValueError: Значение 73 должно быть меньше 42
#del std_one.age # AttributeError: Свойство "_age" нельзя удалять
print(f'{std_one.__dict__ = }')


# 6. Экономим память
# Мы уже несколько раз сталкивались с дандер словарём __dict__. Его
# предназначение — хранить атрибуты и их значения у каждого объекта Python.
# Хранитель атрибутов __dict__
# Рассмотрим уже знакомый по прошлой лекции класс Triangle и выведем на печать
# содержимое __dict__ у экземпляра и у класса.

from math import sqrt
class Triangle:
    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self._a}, {self._b}, {self._c}'
    def __repr__(self):
        return f'Triangle({self._a}, {self._b}, {self._c})'
    
    def __eq__(self, other):
        first = sorted((self._a, self._b, self._c))
        second = sorted((other._a, other._b, other._c))
        return first == second
    def area(self):
        p = (self._a + self._b + self._c) / 2
        _area = sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
        return _area
    def __lt__(self, other):
        return self.area() < other.area()
    def __hash__(self):
        return hash((self._a, self._b, self._c))
triangle = Triangle(3, 4, 5)
print(triangle)
#print(triangle.__dict__)
print(Triangle.__dict__)
