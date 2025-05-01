# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

class MyString(str):
    """
    класс Моя Строка, где: будут доступны все возможности str
    и дополнительно хранятся имя автора строки и время создания
    """
    def __new__(cls,name,value):
        import time
        inst= super().__new__(cls,value)
        inst.name = name
        inst.time=time.time()
        print(f'Create class: {cls} {name=}, {inst.time=}')
        return inst

mystring=MyString('Steve','Hello world')
print(mystring)

# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """
    класс Архив, который хранит число и строку.
       При нового экземпляра класса, старые данные из ранее
       созданных экземпляров сохраняются в пару списковархивов
       list-архивы также являются свойствами экземпляра
    """
    _inst=None

    def __init__(self, num,text):
        self.num = num
        self.text =text
    
    def __new__(cls, *args, **kwargs):
        if cls._inst is None:
            cls._inst=super().__new__(cls)
            cls._inst.list_num=[]
            cls._inst.list_text=[]
        else:
           cls._inst.list_num.append(cls._inst.num) 
           cls._inst.list_text.append(cls._inst.text)
        return cls._inst
    def __str__(self):
        return f'Числа {self.list_num}  Текст - {self.list_text}'
    def __repr__(self):
        return f'User({self.num}, "{self.text}")'

arh=Archive(2,'Two')
arh1=Archive(3,'Tri')
arh2=Archive(4,'For')
print(arh2, arh2.num, arh2.text)
print(repr(arh2))

# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.