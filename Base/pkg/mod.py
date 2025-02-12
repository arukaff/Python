from sys import argv

__all__=['testprint']


def testprint(s='Hello world'):
    print(s)

# Задание №7
# � Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию

def _is_leap(year:int) ->bool: #защищённую функцию
    return year % 400 ==0 or year % 4==0 and year % 100 !=0


def is_valid_date(date: str) -> bool:
    day, month, year = map(int,date.split('.'))
    if year<1 or year>9999 or month< 1 or month>12 or day<1 or day>31:
        return False
    elif month in (1,3,5,7,8,10,12):
        return day < 32
    elif month in (4,6,9,11):
        return day < 31
    elif _is_leap(year):
        return day <30
    else:
        return day <29

 # Задание 1. Модуль для подсчета количества повторений слов
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.


def set_dict(sl: list) -> dict:
    res_dict={}
    for s in sl:
        res_dict[s]=int(res_dict.get(s,0))+1
    return res_dict


if __name__== '__main__':
    print(argv[1:])
    testprint('Проверка')
    print(is_valid_date('29.02.2025'))
    print(set_dict(['ddd','sss','ddd','ddd','sss','aaa']))

