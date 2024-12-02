# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году

# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta

def current_time():
    now=datetime.now()
    f_date=now.strftime('%Y-%m-%d %H:%M:%S')
    d_of_w=now.strftime('%A')
    w_number = now.isocalendar()[1]

    print(f'Текущее дата и время: {f_date}')
    print(f'День недели: {d_of_w}')
    print(f'Номер недели: {w_number}')

def future_date(d):
    now=datetime.now()
    f_data = now + timedelta(days=d)
    print(f'Текущая дата плюс {d} дней : {f_data.strftime('%Y-%m-%d')}')

   

if __name__ == '__main__':
    current_time()
    future_date(30)