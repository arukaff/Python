# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

from collections import deque
import json
import time

class Factorial:

    def __init__(self, k):
        self.memory = deque(maxlen=k)

    def __call__(self, n, *args, **kwds):
        res =1
        for num in range(2,n+1):
            res *=num
        self.memory.append({n:res})
        return self.memory[-1]
    def old(self):
        return self.memory
    
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dic={}
        while self.memory:
            dump_dic.update(self.memory.popleft())
        with open(f'{int(time.time())}.json', 'w', encoding='utf-8') as f:
            json.dump(dump_dic,f)

f=Factorial(3)
for i in range(2,20,2):
    print(f(i))
    print(f.old())
with f as s:
    s(5)

# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Fact():
    def __init__(self, *args):
        match len(args):
            case 3:
                self.start, self.stop, self.step = args
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start < self.stop:
            res =1
            for num in range(2,self.start+1):
                res *=num 
            self.start +=self.step
            return res
        raise StopIteration
fact=Fact(5)
for num in fact:
    print(num, end=' ')

# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных). Используйте декораторы свойств

# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.
class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def validate(self, value):
        if value< 1:
            raise ValueError(f'Значение {value} должно быть >0')
        
        
class Rectangle:
    __slots__ = ('_width', '_height')
    def __init__(self, width, height=None):
        # Если высота не указана, устанавливаем ее равной ширине  (создаем квадрат)
        self._width = width
        self._height = height if height is not None else width



    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value>0:
            self._width=value
        else:
            raise ValueError('Ширина должна быть положительная')
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value>0:
            self._height=value
        else:
            raise ValueError('Длинна  должна быть положительная')
        

    # Метод для вычисления периметра прямоугольника
    def perimeter(self):
        return 2 * (self.width + self.height)
    # Метод для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height
    # Магический метод для сложения двух прямоугольников
    def __add__(self, other):
    # Сложение периметров
        new_perimeter = self.perimeter() + other.perimeter()
    # Обратный расчет сторон для нового прямоугольника
        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)
    # Магический метод для вычитания одного прямоугольника из   другого
    def __sub__(self, other):
        # Вычитание периметров
        new_perimeter = abs(self.perimeter() - other.perimeter())
        # Обратный расчет сторон для нового прямоугольника
        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)
    # Метод сравнения по площади (меньше)
    def __lt__(self, other):
        return self.area() < other.area()
    # Метод сравнения на равенство по площади
    def __eq__(self, other):
        return self.area() == other.area()
    # Метод сравнения по площади (меньше или равно)
    def __le__(self, other):
        return self.area() <= other.area()
    # Строковое представление прямоугольника для пользователя
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"
    # Строковое представление прямоугольника для разработчика
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
rect = Rectangle(3,5)
print(rect)
print(Rectangle.__dict__)
#rect.width=0