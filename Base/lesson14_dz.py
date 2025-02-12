# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.

import os
def batch_rename_files(directory, final_name, num_digits,old_extension, new_extension, name_range):
    """
    Переименовывает файлы в указанном каталоге.
    :param directory: Путь к каталогу с файлами.
    :param final_name: Конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param old_extension: Расширение исходного файла.
    :param new_extension: Расширение конечного файла.
    :param name_range: Диапазон сохраняемого оригинального имени
    (начало, конец).
    """
    # Проверяем существование каталога
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")
    # Получаем список файлов с указанным расширением
    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
    if not files:
        print("Файлы с указанным расширением не найдены.")
        return
    # Определяем формат номера с ведущими нулями
    format_string = f"{{:0{num_digits}d}}"
    # Перебираем файлы и переименовываем их
    for index, file_name in enumerate(files, start=1):
        # Извлекаем базовое имя файла без расширения
        base_name = os.path.splitext(file_name)[0]
        # Извлекаем часть имени файла по заданному диапазону
        if name_range:
            start, end = name_range
            extracted_name = base_name[start-1:end] # Индексы диапазона начинаются с 0
        else:
            extracted_name = base_name
        # Формируем новое имя файла
        new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
        # Полные пути для старого и нового файла
        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)
        # Переименование файла
        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{file_name}' в '{new_file_name}'")

# Пример использования функции
if __name__ == "__main__":
    import sys
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 6:
        print("Usage: python file_rename.py <directory> <final_name> <num_digits> <old_extension> <new_extension>")
        sys.exit(1)
        directory = sys.argv[1]
        final_name = sys.argv[2]
        num_digits = int(sys.argv[3])
        old_extension = sys.argv[4]
        new_extension = sys.argv[5]
        # Например, диапазон [3, 6]
        name_range = [3, 6]
        batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range)

# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
# должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
# должен включать все файлы и подпапки исходного каталога.
import zipfile


def zip_directory(source_dir, output_zip):
    """
    Создает архив .zip из указанного каталога.
    :param source_dir: Путь к исходному каталогу для архивирования.
    :param output_zip: Путь к целевому архиву .zip.
    """
    # Создаем объект ZipFile для записи архива
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Проходим по всем файлам и папкам в исходном каталоге
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Полный путь к текущему файлу
                file_path = os.path.join(root, file)
                # Добавляем файл в архив с путем относительно исходного каталога
                zipf.write(file_path, os.path.relpath(file_path,source_dir))


# Пример использования функции
zip_directory('/path/to/source_dir', '/path/to/output.zip')

# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.
import time
def delete_old_files(directory, days_old):
    """
    Удаляет файлы в указанном каталоге, которые не изменялись более
    заданного количества дней.
    :param directory: Путь к каталогу, в котором нужно удалить
    старые файлы.
    :param days_old: Количество дней, после которых файлы считаются
    старыми.
    """
    now = time.time() # Текущее время в секундах с начала эпохи
    cutoff = now - (days_old * 86400) # Преобразуем количество дней в секунды (86400 секунд в дне)
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file) # Полный путь к файлу
            file_mod_time = os.path.getmtime(file_path) # Время последнего изменения файла
            # Если время последнего изменения меньше порогового значения, удаляем файл
            if file_mod_time < cutoff:
                os.remove(file_path) # Удаляем файл
                print(f"Удален файл: {file_path}")
# Пример использования функции
delete_old_files('/path/to/directory', 30)


# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.

def find_files_by_extension(directory, extension):
    """
    Находит и перечисляет все файлы с заданным расширением в
    указанном каталоге и всех его подкаталогах.
    :param directory: Путь к каталогу, в котором нужно искать файлы.
    :param extension: Расширение файлов для поиска (например,
    '.txt').
    """
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
        # Проверяем, заканчивается ли имя файла на заданное расширение
            if file.endswith(extension):
                # Формируем полный путь к файлу и выводим его
                print(os.path.join(root, file))


                
# Пример использования функции
find_files_by_extension('/path/to/directory', '.txt')