# Задание 1. Работа с данными студентов
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только
# букв. Если ФИО не соответствует условию, выведите:
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до
# 100). В противном случае выведите:
# Оценка должна быть целым числом от 2 до 5
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по
# оценкам всех предметов вместе взятых.
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
# следующая информация.
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по
# предметам. Класс должен иметь следующие методы:
# Атрибуты класса:
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
# качестве ключей и информацию об оценках и результатах тестов для каждого предмета в
# виде словаря

import csv

class Student:
    def __init__(self, name, subjects_file):
        # Устанавливаем ФИО с помощью дескриптора
        self.__setattr__('name', name)
        self.subjects = {}
        # Загружаем предметы из файла
        self.load_subjects(subjects_file)
    def __setattr__(self, name, value):
        # Проверяем ФИО на правильность
        if name == 'name':
            if not (value and value[0].isupper() and value.replace(" ", "").isalpha()):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)
    def __getattr__(self, name):
        # Возвращаем предмет из словаря, если он существует
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f"Предмет {name} не найден")
    def __str__(self):
        # Формируем строковое представление студента и его предметов
        subject_list = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subject_list}"
    def load_subjects(self, subjects_file):
        try:
        # Читаем предметы из файла CSV
            with open(subjects_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    subjects = [subject.strip() for subject in row]
                    for subject in subjects:
                        if subject:
                            self.subjects[subject] = {'grades': [], 'test_scores': []}
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {subjects_file} не найден")
    def add_grade(self, subject, grade):
        # Добавляем оценку по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(grade, int) and 2 <= grade <= 5):
            print("Оценка должна быть целым числом от 2 до 5")
            return
        self.subjects[subject]['grades'].append(grade)
    def add_test_score(self, subject, test_score):
    # Добавляем результат теста по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(test_score, int) and 0 <= test_score <=  100):
            print("Результат теста должен быть целым числом от 0 до 100")
            return
        self.subjects[subject]['test_scores'].append(test_score)
    def get_average_test_score(self, subject):
    # Возвращаем средний балл по тестам для заданного предмета
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return None
        scores = self.subjects[subject]['test_scores']
        if not scores:
            return 0.0
        return sum(scores) / len(scores)
    def get_average_grade(self):
    # Возвращаем средний балл по всем предметам
        all_grades = [grade for sub in self.subjects.values() for grade in sub['grades']]
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)
# Пример использования
if __name__ == "__mein__":
# Создаем экземпляр студента, загружаем предметы из файла subjects.csv
    student = Student("Иван Иванов", "subjects.csv")
    # Добавляем оценки и результаты тестов
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    # Получаем средний балл и результат по тестам
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score =  student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    # Выводим информацию о студенте
    print(student)

# Задача 2. Класс с валидацией данных
# Создайте класс Person, который имеет атрибуты name, age, и email. При
# установке значения атрибута name, оно должно начинаться с заглавной буквы.
# При установке значения атрибута age, оно должно быть целым числом в
# диапазоне от 0 до 120. При установке значения атрибута email, оно должно
# содержать символ @.
class Person:
    def __setattr__(self, name, value):
        if name == 'name':
            if not (value and value[0].isupper() and  value.isalpha()):
                raise ValueError("Имя должно начинаться с заглавной буквы и состоять из букв")
        elif name == 'age':
            if not (isinstance(value, int) and 0 <= value <= 120):
                raise ValueError("Возраст должен быть целым числом от 0 до 120")
        elif name == 'email':
            if '@' not in value:
                raise ValueError("Электронная почта должна содержать символ '@'")
        super().__setattr__(name, value)
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"
# Пример использования
try:
    p = Person()
    p.name = "John"
    p.age = 25
    p.email = "john@example.com"
    print(p)
except ValueError as e:
    print(e)

# Задача 3. Класс с динамическим созданием экземпляров
# Создайте класс Book, который создает экземпляры с помощью __new__. Убедитесь,
# что каждый экземпляр имеет уникальный идентификатор.
class Book:
    _id_counter = 1
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book(ID={self.id}, title={self.title}, author={self.author})"
# Пример использования
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(book1)
print(book2)

# Задача 4. Класс с контролем цены и количества
# Создайте класс Product с атрибутами name, price, и quantity. price должен
# быть положительным числом, а quantity неотрицательным целым числом. При
# попытке установить price или quantity, должен производиться контроль
# значений.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __setattr__(self, name, value):
        if name == 'price':
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError("Цена должна быть положительным  числом")
        elif name == 'quantity':
            if not (isinstance(value, int) and value >= 0):
                raise ValueError("Количество должно быть  неотрицательным целым числом")
        super().__setattr__(name, value)
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
# Пример использования
try:
    prod = Product("Laptop", 1000, 10)
    prod.price = 1200
    prod.quantity = 5
    print(prod)
except ValueError as e:
    print(e)