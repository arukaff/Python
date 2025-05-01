with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8',
    errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)

# Чтение циклом for Вместо метода readline без аргумента можно использовать более короткую запись с циклом for
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
# Файл построчно попадает в переменную line. А для того чтобы избавиться от пустых
# строк отключили перенос строки в функции print.
# 🔥 Важно! Символ переноса строки сохранился в конце каждой строки.
# Если вам необходимо обработать строку без переносов, можно использовать
# срезы line[:-1] или метод замены line.replace('\n', '')

with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))

# ● Запись методом write
# Метод write принимает на вход строку или набор байт в зависимости от того как вы
# открыли файл. После записи метод возвращает количество записанной
# информации.
text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.', 'Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?','Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')
# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n
text = ['Lorem ipsum dolor sit amet, consectetur adipisicingelit.','Consequatur debitis explicabo laboriosam sint suscipittemporibus veniam?','Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')

# ● Запись методом writelines
# Метод writelines принимает в качестве аргумента последовательность и записывает
# каждый элемент в файл. Элементы последовательности должны быть строками или
# байтами в зависимости от режима записи.
# 12
# В отличии от write этот метод ничего не возвращает.
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
# Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
# воспользовались строковым методом join. writelines не добавляет переноса между
# элементами последовательности.
# ● print в файл
# Функция print по умолчанию выводит информацию в поток вывода. Обычно это
# консоль. Но можно явно передать файловый объект для печати в файл. Для этого надо воспользоваться ключевым параметром le.
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
# В отличии от методов записи в файл, функция print добавляет перенос строки.
# Кроме того ничто не мешает явно изменить параметр end функции.
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)


# ● Метод tell
# Метод tell возвращает текущую позицию в файле.
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
print(f.tell()) # ValueError: I/O operation on closed file.
# Для пустого файла возвращается ноль — начало файла. По мере записи или чтения
# информации позиция сдвигается к концу файла.
# Метод использую для определения в каком месте файла будет произведены чтение
# или запись.

# ● Метод seek
# Метод seek позволяет изменить положение “курсора” в файле.
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
# способ выбора опороной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла
# 🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными
# файлами. Исключение seek(0, 2) для перехода в конец текстового файла.
# 14
# Метод возвращает новую позицию “курсора”.
last = before = 0

with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
        print(f'{f.seek(before, 0) = }')
        f.write('\n'.join(text))

# В примере выше мы открыли текстовый файл для одновременного чтения и записи.
# Переменные last и before хранят позиции двух последних прочитанных строк.
# Дочитав файл в цикле while до конца изменяем позицию “курсора” на начало
# последней строки и начинаем запись. Таким образом мы сохранили все строки
# файла кроме последней и записали новый текст в конец.


# ● Метод truncate
# truncate(size=None) — метод изменяет размер файла. Если не передать значение в
# параметр size будет удалена часть файла от текущей позиции до конца. Метод
# возвращает позицию после изменения файла.
last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f.seek(before, 0))
        print(f.truncate())

# Если передать параметр size метод изменяет размер файла до указанного числа
# символов или байт от начала файла.
size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))

#Если size меньше размера файла, пр


# ● Текущий каталог
# Для получения информации о текущем каталоге можно использовать модуль os или pathlib
import os
from pathlib import Path
print(os.getcwd())
print(Path.cwd())

os.chdir('../..')
print(os.getcwd())
print(Path.cwd())

# ● Создание каталогов
# Для создания каталога снова можно воспользоваться двумя модулями

os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()
# Представленный код создаёт каталог в текущей директории. А если необходимо
# создать несколько вложенных друг в друга каталогов, код будет следующим:

os.makedirs('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# ● Удаление каталогов
# Для удаления одного каталога подойдут следующие функция и метод

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()
# 🔥 Важно! Удалить можно лишь пустой каталог. Если внутри удаляемого
# каталога есть другие каталоги или файлы, возникнет ошибка OSError.
# Обратите внимание, что при передаче цепочки каталогов удаляется один,
# последний из перечисленных. Родительские каталоги остаются без изменений.
# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и
# файлы), подойдёт функция из модуля shutil
import shutil
shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
# В первом случае будет удалена директория other_dir со всем содержимым.
# Директория dir останется на месте.

# ● Формирование пути
# В операционной системе Windows для указания пути используется обратный слеш \.
# В Unix системах путь разделяется слешем. Чтобы программа работала одинаково на
# любой ОС рекомендуется использовать специальную функцию join из os.path для
# склеивания путей.
# Модуль pathlib использует более понятный приём с переопределением операции
# деления.

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

# Чтение данных о каталогах
# Для получения информации о том какие директории и файлы находятся в текущем
# каталоге можно воспользоваться следующими вариантами кода.

print(os.listdir())
p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
# Функция listdir возвращает список файлов и каталогов. Метод iterdir у экземпляра
# класса Path является генератором. В цикле он возвращает объекты из выбранной
# директории.

#Проверка на директорию, файл и ссылку

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')
p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')


for dir_path, dir_name, le_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{le_name = }\n')


# Работа с файлами
# Рассмотрим базовые операции по работе с файлами как с отдельными объектами.
# ● Переименование файлов
# Переименование файла подразумевает сохранение неизменным файла в файловой
# таблице и в содержимом файла, но изменение его имени. Для переименования
# можно воспользоваться следующим кодом.

os.rename('old_name.py', 'new_name.py')
p = Path('old_file.py')
p.rename('new_file.py')
Path('new_file.py').rename('newest_file.py')


# ● Перемещение файлов
# Перемещение файла подразумевает изменение его позиции в каталоге файловой
# системы. В процессе перемещения файл может быть переименован.

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir','new_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# ● Копирование файлов
# Для копирования файлов лучше всего подходит модуль shutil, который
# предоставляет ряд высокоуровневых операций.
import shutil
shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')
# Функции copy и copy2 работают схожим образом. Они принимают файл для
# копирования и целевой каталог. Если такого каталога не существует, функция
# попытается присвоить копируемому файлу имя “цели”.
# Отличие состоит в том, что функция copy2 помимо содержимого файла пытается
# скопировать и связанные с ним метаданные.
# Если стоит задача скопировать каталог со всем его содержимым в новое место,
# модуль предоставляет функции copytree.

shutil.copytree('dir', 'one_more_dir')
# Функция copytree рекурсивно обходит указанный каталог и копирует его
# содержимое в новое место.

# ● Удаление файлов
# Вариант удаления всего каталога целиком с содержимым мы уже рассматривали
# сегодня.

shutil.rmtree('dir')
# Если же необходимо удалить один файл, можно воспользоваться следующими
# вариантами:

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
# И функция remove и метод unlink пытаются удалить файл по указанному пути.
