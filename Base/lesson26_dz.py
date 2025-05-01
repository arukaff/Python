# Задание 1. Карма
# Один буддист-программист решил создать свой симулятор жизни, в котором
# нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
# Каждый день вызывается специальная функция one_day(), которая возвращает
# количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
# исключений:
# ● KillError,
# ● DrunkError,
# ● CarCrashError,
# ● GluttonyError,
# ● DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от
# Exception.)
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
# которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.


import random
# Константа для достижения просветления
NIRVANA_KARMA = 500
# Определение пользовательских исключений
class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")
class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")
class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за  дорогой.")
class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")
class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")
# Функция, моделирующая один день жизни
def one_day():
    # Случайное количество кармы от 1 до 7
    day_karma = random.randint(1, 7)
    # Случайная вероятность выброса исключения
    if random.randint(1, 10) == 5:
    # Случайный выбор исключения
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma
# Основная функция симулятора
def main():
    karma = 0
    # Открываем файл для записи логов
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                # Прибавляем карму за один день
                karma += one_day()
            except Exception as ex:
                 # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')
                # Проверяем, достигнуто ли необходимое количество кармы
            if karma >= NIRVANA_KARMA:
                break
    # Сообщаем о достижении цели
    print('Вы достигли Нирваны! ')
    print('Омм ')
# Запуск основной функции
if __name__ == "__main__":
    main()

# Задача 2. Чат
# Реализуйте программу - чат, в котором могут участвовать сразу несколько человек, то
# есть программа может работать одновременно для нескольких пользователей. При
# запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
# 1. Посмотреть текущий текст чата
# 2. Отправить сообщение (затем вводит сообщение) Действия запрашиваются
# бесконечно.

class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename
    def display_messages(self):
        """Отображает все сообщения из файла."""
        try:
            with open(self.filename, 'r') as file:
                messages = file.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("Служебное сообщение: пока что ничего нет\n")
    def add_message(self, name, message):
        """Добавляет новое сообщение в файл."""
        with open(self.filename, 'a') as file:
            file.write(f"{name}: {message}\n")
    def run(self):
        """Запускает основной цикл чата."""
        name = input("Как вас зовут? ")
        while True:
            print("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2")
            response = input("Введите 1 или 2: ")
            if response == '1':
                self.display_messages()
            elif response == '2':
                new_message = input("Введите сообщение: ")
                self.add_message(name, new_message)
            else:
                print("Неизвестная команда\n")
# Запуск программы
if __name__ == "_1_main__":
    chat = Chat()
    chat.run()

# Задача 3. Счастливое число
# Напишите программу, которая запрашивает у пользователя число до тех пор, пока
# сумма этих чисел не станет больше либо равна 777. Каждое введенное число при этом
# дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
# вероятностью 1 к 13 выбрасывала пользователю случайное исключение и
# завершалась.

import os
import random
MAGIC_NUMBER = 777
class MagicFileProcessor:
    def __init__(self, filename):
        """Инициализация с именем файла и определение пути к  файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0
    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return os.path.join(os.path.abspath('.'), self.filename)
    def is_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать  ошибку."""
        return random.randint(1, 13) == 7
    def pre_init(self):
        """Удаляет файл, если он существует."""
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')
    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в  файл."""
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')
        except (ValueError, KeyboardInterrupt) as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')
    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.pre_init() # Удаляет старый файл, если он существует
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    # Запуск программы
if __name__ == "_1_main__":
    processor = MagicFileProcessor('out_file.txt')
    processor.run()


# Задача 4. Счетчик Очков в Игрe
# Создайте класс GameScore для отслеживания очков игрока. В этом классе
# должны быть методы для добавления и уменьшения очков. Однако:
# ● Очки не могут быть отрицательными.
# ● Если игрок пытается добавить больше очков, чем 1000, должно быть
# выброшено исключение ScoreLimitExceededError.
# Создайте пользовательское исключение ScoreLimitExceededError.

class ScoreLimitExceededError(Exception):
    """Исключение, выбрасываемое при попытке добавить очки, превышающие лимит."""
    def __init__(self):
        super().__init__("Очки не могут быть больше 1000.")
class GameScore:
    """Класс для отслеживания очков игрока с ограничениями."""
    def __init__(self):
        """Инициализирует начальное значение очков."""
        self.score = 0
    def add_score(self, points):
        """Добавляет очки к текущему счету, проверяя лимит."""
        if self.score + points > 1000:
            raise ScoreLimitExceededError()
        self.score += points
    def subtract_score(self, points):
        """Уменьшает очки, проверяя, чтобы счет не стал  отрицательным."""
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points
# Пример использования класса GameScore:
game_score = GameScore()
try:
    # Добавляем 500 очков
    game_score.add_score(500)
    print(f"Текущий счет: {game_score.score}")
    # Пытаемся добавить еще 600 очков, что вызовет исключение
    game_score.add_score(600)
except ScoreLimitExceededError as e:
    print(e)
except ValueError as e:
    print(e)
try:
    # Пытаемся вычесть больше очков, чем есть
    game_score.subtract_score(600)
except ValueError as e:
    print(e)
# Проверка работы метода subtract_score
try:
    game_score.subtract_score(100)
    print(f"Текущий счет после вычитания: {game_score.score}")
except ValueError as e:
    print(e)


# Задача 5. Валидатор Пользовательских Данных
# Создайте класс User, который содержит атрибуты name, email, и age.
# Необходимо убедиться, что:
# ● Имя состоит из хотя бы двух слов, каждое из которых начинается с
# заглавной буквы.
# ● Электронная почта содержит символ @ и точку . после @.
# ● Возраст — это положительное целое число, не меньше 0 и не больше
# 120.
# Создайте пользовательские исключения для каждой из этих проверок:
# ● NameError: Если имя не соответствует формату.
# ● EmailError: Если электронная почта не соответствует формату.
# ● AgeError: Если возраст вне допустимого диапазона.

class NameError(Exception):
    def __init__(self):
        super().__init__("Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы.")
class EmailError(Exception):
    def __init__(self):
        super().__init__("Электронная почта должна содержать символ  '@' и точку '.' после '@'.")
class AgeError(Exception):
    def __init__(self):
        super().__init__("Возраст должен быть целым числом от 0 до    120.")
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not (len(value.split()) >= 2 and all(word[0].isupper() for word in value.split())):
            raise NameError()
        self._name = value
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value.split('@')[1]:
            raise EmailError()
        self._email = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and 0 <= value <= 120):
            raise AgeError()
        self._age = value
# Пример использования:
try:
    user = User(name="John Doe", email="john.doe@example.com",age=25)
    print(f"User created: {user.name}, {user.email}, {user.age}")
except (NameError, EmailError, AgeError) as e:
    print(e)