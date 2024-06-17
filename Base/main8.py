
# Задача №49. 
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('Телефон: ')
            print(find_by_number(phone_book,number))
        elif choice==4:
            user_data={} #fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
            user_data['Фамилия']=input('Фамилия: ')
            user_data['Имя']=input('Имя: ')
            user_data['Телефон']=input('Телефон: ')
            user_data['Описание']=input('Описание: ')
            print(add_user(phone_book,user_data))
        elif choice==5:
            lastname=input('Фамилия: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==6:
            last_name=input('Фамилия: ')
            new_number=input('Новый номер: ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==7:
            write_txt('phon.txt',phone_book)
            break


        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
		  "5. Удалить абонента из справочника\n"
          "6. Изменить номер абонента\n"
          "7. Закончить работу и сохранить изменения\n"
          "8. Выйти без сохранения\n")
    choice = int(input())
    return choice

def print_result(phone_book):
    print('   '.join(phone_book[0].keys()))
    for i in phone_book:  
        print('   '.join(i.values()))
   
def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия']==last_name:
            return '   '.join(i.values())
    return 'Нет такой записи'

def find_by_number(phone_book,number):
    for i in phone_book:
        if i['Телефон']==number:
            return '   '.join(i.values())
    return 'Нет такой записи'


def change_number(phone_book,last_name,new_number):
    for i in phone_book:
        if i['Фамилия']==last_name:
            s=i['Телефон']
            i['Телефон']=new_number
            return 'Номер абонента  '+i['Фамилия']+' изменен с '+s+' на '+new_number
    return 'Нет такой Фамилии'
    
def delete_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия']==last_name:
            phone_book.pop(phone_book.index(i))
            return 'Запись '+'   '.join(i.values())+'  удалена из справочника'
    return 'Нет такой записи'


def add_user(phone_book,user_data):
    phone_book.insert(0,user_data)
    return 'Запись '+'   '.join(user_data.values())+'  добавлена в справочник'

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           line = ''.join(line.split())
           if line!='':
                record = dict(zip(fields, line.split(','))) 	
                phone_book.append(record)	
    return phone_book

def write_txt(filename, phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')




work_with_phonebook()
