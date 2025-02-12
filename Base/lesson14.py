# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random
from pathlib import Path

MIN=-1000
MAX= 1000


def write_random_to_file(num:int,file_name: str | Path)->None:
    with open(file_name,'a') as f:
        for _ in range(num):
            f.writelines(f'{random.randint(MIN,MAX):>4} |{random.uniform(MIN,MAX)}\n')


write_random_to_file(10,'random.txt')


# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

VOWELS='eyuioa'
CONS='qwrtpsdfghjklzxcvbnm'
MIN_l=4
MAX_l=7
from random import choice, randint

def gen_name(count:int,file_name:str|Path)->None:
    for _ in range(count):
        name = ''.join(choice(VOWELS) if i in (randint(0,i)) else choice(CONS))


# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from typing import TextIO

def read_or_begin(fd: TextIO)-> str:
    text = fd.readline()
    if text =='':
        fd.seek(0)
        text=fd.readline()
    return text.split()


def convert(num: str, names: str, result: str)-> None:
    with (
        open(num,'r', encoding='utf-8') as f_num,
        open(names,'r', encoding='utf-8') as f_nam,
        open(result,'w',encoding='utf-8') as f_res
    ):
        len_n= sum(1 for _ in f_nam)
        len_nu=sum(1 for _ in f_num)
        for _ in range(max(len_n,len_nu)):
            num_str=read_or_begin(f_num)
            name=read_or_begin(f_nam)
            num_i, num_f = num_str.split('|')
            res= int(num_i) * float(num_f)
            if res<0:
                f_res.write(f'{name.lower()} {-res}\n')
            else:
                f_res.write(f'{name.upper()} {int(res)}\n')


# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
def create_files(ext,count):
    print(ext,count)


# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
from os import chdir


def gen_files(path: str|Path, **kwards) ->None:
    if isinstance(path,str):
        path=Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)# меняем директорию на созданную
    for ext, count in kwards.items():
        create_files(ext,count)

gen_files('c:\\Users\\rukavishnikovav\\Python\\Base\\new', jpg=2, txt=2, bin=1)

# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

def sort_files(path: Path, groups:dict[Path, list[str]]=None)->None:
    chdir(path)
    if groups is None:
        groups= {
            Path('Video'): ['mp4','mov','mkv'],
            Path('Images'): ['png','jpg','jpeg']
        }
    reverse_proups ={}
    for target_dir, ext_lst in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True)
        for ext in ext_lst:
            reverse_proups[ext]=target_dir

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_proups:
            file.replace(reverse_proups[file.suffix]/file.name)