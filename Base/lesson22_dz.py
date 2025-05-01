# Класс Matrix для работы с матрицами
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Инициализация матрицы нулями
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    # Метод для сложения двух матриц
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают для сложения")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] +   other.data[i][j]
        return result
    # Метод для вычитания двух матриц
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают для  вычитания")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result
    # Метод для умножения двух матриц
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] *other.data[k][j]
        return result
    # Метод для транспонирования матрицы
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result
    # Метод для красивого вывода матрицы на экран
    def __str__(self):
        # Форматирование строк матрицы
        res = "\n".join(["\t".join(map(str, row)) for row in self.data])
        return res

# Примеры работы с классом:
# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
print(m1.data)
m1.data = [[1, 2, 3], [4, 5, 6]]
m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]
# Тестирование операций
print("Матрица 1:")
print(m1)
print("Матрица 2:")
print(m2)
print("Сложение матриц:")
print(m1.add(m2))
print("Вычитание матриц:")
print(m1.subtract(m2))
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print("Умножение матриц:")
print(m1.multiply(m3))
print("Транспонирование матрицы 1:")
print(m1.transpose())

# Задача 2. Магия
# Для одной игры необходимо реализовать механику магии, где при соединении
# двух элементов получается новый. У нас есть четыре базовых элемента:
# «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
# «Пар», «Грязь», «Молния», «Пыль», «Лава».
# Таблица преобразований:
# ● Вода + Воздух = Шторм;
# ● Вода + Огонь = Пар;
# ● Вода + Земля = Грязь;
# ● Воздух + Огонь = Молния;
# ● Воздух + Земля = Пыль;
# ● Огонь + Земля = Лава.
# Напишите программу, которая реализует все эти элементы. Каждый элемент
# необходимо организовать как отдельный класс. Если результат не определён,
# то возвращается None.
import random
TRIES = 10
# Определение производных элементов
class Storm:
    answer = "Вы сложили Воду и Воздух и получили класс Шторм"
class Steam:
    answer = "Вы сложили Воду и Огонь и получили класс Пар"
class Mud:
    answer = "Вы сложили Воду и Землю и получили класс Грязь"
class Bolt:
    answer = "Вы сложили Воздух и Огонь и получили класс Молния"
class Dust:
    answer = "Вы сложили Воздух и Землю и получили класс Пыль"
class Lava:
    answer = "Вы сложили Огонь и Землю и получили класс Лава"
# Дополнительный элемент
class Fog:
    answer = "Вы сложили Воду и Пыль и получили класс Туман"

# Определение базовых элементов
class Water:
    def __add__(self, other):
        if isinstance(other, Soil):
            return Mud()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Dust):
            return Fog() # Взаимодействие Воды и Пыли
class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Bolt()
        elif isinstance(other, Soil):
            return Lava()
class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Bolt()
        elif isinstance(other, Soil):
            return Dust()
class Soil:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
# Основная функция
def main():
    elements = [Water(), Fire(), Air(), Soil()] # Добавили   элемент Пыль для взаимодействия
    try_count = 0
    while try_count < TRIES:
        element_a = random.choice(elements)
        element_b = random.choice(elements)
        result = element_a + element_b
        if result is None:
            continue
        try_count += 1
        print(result.answer)
        print()
main()

# Задача 3. Класс Rectangle - работа с прямоугольниками
# Разработайте программу для работы с прямоугольниками. Необходимо создать класс
# Rectangle, который будет представлять прямоугольник с заданными шириной и высотой

class Rectangle:
    def __init__(self, width, height=None):
        # Если высота не указана, устанавливаем ее равной ширине  (создаем квадрат)
        self.width = width
        self.height = height if height is not None else width
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
# Примеры работы с классом Rectangle
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
# Вывод периметра и площади
print(f"Периметр rect1: {rect1.perimeter()}") # Вывод: 30
print(f"Площадь rect2: {rect2.area()}") # Вывод: 21
# Сравнение прямоугольников по площади
print(f"rect1 < rect2: {rect1 < rect2}") # Вывод: False
print(f"rect1 == rect2: {rect1 == rect2}") # Вывод: False
print(f"rect1 <= rect2: {rect1 <= rect2}") # Вывод: False
# Сложение и вычитание прямоугольников
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}") # Вывод: 50
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}") # Вывод: 2
# Дополнительный тест для repr и str
print(rect3) # Вывод: Прямоугольник со сторонами 12 и 12
print(repr(rect4)) # Вывод: Rectangle(2, 2)


# Задача 4. Стек
# В программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых
# структур является стек.
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл —
# первым вышел»).
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой
# видна, является самая верхняя. Чтобы получить доступ, например, к третьей
# снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
# Напишите класс, который реализует стек и его возможности (достаточно будет
# добавления и удаления элемента).
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач
# можно выполнить команду «новая задача», в которую передаётся сама задача
# (str) и её приоритет (int). Сам менеджер работает на основе стека (не
# наследование). При выводе менеджера в консоль все задачи должны быть
# отсортированы по следующему приоритету: чем меньше число, тем выше задача

class Stack:
    def __init__(self):
        # Инициализация стека как пустого списка
        self.__stack = list()
    def pop(self):
        # Извлечение элемента из стека, если он не пуст
        if self.is_empty():
            return None
        return self.__stack.pop()
    def push(self, item):
        # Добавление элемента в стек
        self.__stack.append(item)
    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.__stack) == 0
    def top(self):
        # Получение верхнего элемента стека без удаления
        if self.is_empty():
            return None
        return self.__stack[-1]
    
class TaskManager:

    def __init__(self):
        # Инициализация словаря для хранения стека задач по приоритетам
        self.tasks = dict()
    def new_task(self, text, priority):
        # Добавление новой задачи в стек с заданным приоритетом
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
            # Добавляем задачу в стек для данного приоритета
        self.tasks[priority].push(text)
    def remove_task(self, text):
        # Удаление задачи по тексту из всех стеков
        for stack in self.tasks.values():
            # Используем временный стек для хранения задач, которые не нужно удалять
            temp_stack = Stack()
            while not stack.is_empty():
                task = stack.pop()
                if task != text:
                    temp_stack.push(task)
            # Перемещаем оставшиеся задачи обратно в основной стек
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())
    def __str__(self):
        # Отображение задач, отсортированных по приоритету
        sorted_keys = sorted(self.tasks.keys())
        out = []
        for key in sorted_keys:
            task_line = [str(key)] # Начинаем строку с приоритета
            temp_stack = Stack()
            while not self.tasks[key].is_empty():
                task = self.tasks[key].pop()
                temp_stack.push(task)
            while not temp_stack.is_empty():
                task_line.append(temp_stack.pop())
                # Добавляем задачи на текущей строке
                out.append(' '.join(task_line))
        return '\n'.join(out)
def main1():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    # Печать списка задач
    print(manager)
    # Удаление задачи и повторный вывод
    manager.remove_task("поесть")
    print("\nПосле удаления задачи:")
    print(manager)
main1()

# Задача 5. Абстрактный класс
# Вы работаете в компании, занимающейся разработкой программного обеспечения
# для архитектурных проектов. Вам необходимо разработать программу для расчёта
# площади различных геометрических фигур, таких как круги, прямоугольники и
# треугольники.
# Задача
# Создайте:
# ● класс Shape, который будет базовым классом для всех фигур и будет
# хранить пустой метод area, который наследники должны переопределить;
# ● класс Circle;
# ● класс Rectangle;
# ● класс Triangle.
# Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод
# для вычисления площади фигуры.

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Абстрактный базовый класс для всех фигур.
    Использует абстрактный метод area, который должен быть
    реализован в дочерних классах.
    """
    @abstractmethod
    def area(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        Должен быть реализован в каждом наследующем классе.
        """
        pass
class Circle(Shape):
    """
    Класс для представления круга, наследует от Shape.
    """
    def __init__(self, radius):
        """
        Инициализация круга с заданным радиусом.
        """
        self.radius = radius
    def area(self):
        """
        Вычисление площади круга.
        Формула: π * радиус^2
        """
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    """
    Класс для представления прямоугольника, наследует от Shape.
    """
    def __init__(self, width, height):
        """
        Инициализация прямоугольника с заданной шириной и высотой.
        """
        self.width = width
        self.height = height
    def area(self):
        """
        Вычисление площади прямоугольника.
        Формула: ширина * высота
        """
        return self.width * self.height
class Triangle(Shape):
    """
    Класс для представления треугольника, наследует от Shape.
    """
    def __init__(self, base, height):
        """
        Инициализация треугольника с заданной основой и высотой.
        """
        self.base = base
        self.height = height
    def area(self):
        """
        Вычисление площади треугольника.
        Формула: 0.5 * основа * высота
        """
        return 0.5 * self.base * self.height
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)
# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()
# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
# Попытка создания экземпляра абстрактного класса Shape (должно вызвать ошибку)
try:
    shape = Shape() # Ожидается ошибка
except TypeError as e:
    print(f"Ошибка: {e}")
