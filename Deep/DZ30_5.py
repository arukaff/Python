# Задача 5. Запуск из командной строки
# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

FileInfo=namedtuple('FileInfo', ['name','extension','is_directory','parent_directory'])
logging.basicConfig(filename='dir_cont.log', level=logging.INFO, format='%(asctime)s -%(message)s')


def collect_info(dir):

    if not os.path.isdir(dir):
        raise ValueError(f'Указанный путь {dir} не является директорией')
    
    parent_dir=os.path.basename(os.path.abspath(dir))

    for e in os.listdir(dir):
        e_path= os.path.join(dir,e)

        if not os.path.isdir(e_path):
            f_info=FileInfo(name=e,extension=None,is_directory=True,parent_directory=parent_dir)

        else:
            name, extension = os.path.splitext(e)
            f_info=FileInfo(name=name,extension=extension.lstrip('.'),is_directory=False,parent_directory=parent_dir)
        
        logging.info(f'{f_info.name} | {f_info.extension} | {f_info.is_directory} | {f_info.parent_directory}')

def main():
    parser= ArgumentParser(description='Собираем данные пишем в лог')
    
    parser.add_argument('directory', type=str, help='Путь до директории')
    
    args=parser.parse_args()

    dir = args.directory

    try:
        collect_info(dir)
        print('Информация успешно записана в файл')

    except ValueError as e:
        print(e)

if __name__ == '__main__':
        main()