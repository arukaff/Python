a = 5
print(type(a), id(a))
a = "hello world"
print(type(a), id(a))
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))

data = 42
print(isinstance(data, int))
#Получили True, т.к. 42 — целое число.
data = True
print(isinstance(data, int))
# Снова истина, т.к. логический объект True в Python подклассом, основанном на
# классе int. Проверка может проходить сразу по нескольким классам. В этом случае
# истину вернётся, если объект является экземпляром любого из переданных в
# кортеже классов.
data = 3.14
print(isinstance(data, (int, float, complex)))

num = 2 + 2 * 2
digit = 36 / 6
print(num , digit)
print(num == digit)
print(num is digit)

a = 5
print(a, id(a))
a += 1
print(a, id(a))

# txt = 'Hello world!'
# txt[5] = '_'
# Получим TypeError: 'str' object does not support item assignment т.к.
# изменить символ в неизменяемой строке нельзя. Но ведь в Python есть
# возможность такой замены.
txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))


a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))


x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
#print(hash(my_list)) # получим ошибку, т.к. list изменяемый

# res= input('Введите текст')
# print(type(res),id(res),hash(res))

def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res
print(my_func([2, 5.5, 15, 8.0, 13.74]))


print("Hello world!".__doc__)
print(str.__doc__)


print(dir("Hello world!"))

# help(str)
# help()

import sys
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    print(num.__sizeof__())
    num *= STEP

text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)
# Такой приём работает, но считается плохим стилем. Плюс, а точнее минус, строки
# соединились без пробелов.
# На этом способы записи строк не заканчиваются. Посмотрите на этот код:
very_long_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab alias animi assumenda at aut ' \
    'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \
    'numquam obcaecati officia officiis porro  possimus praesentium quaerat temporibus ullam veniam? '
print(very_long_text)

empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())

import math
print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(dir(math))

import decimal
pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

decimal.getcontext().prec = 120 #задаю точность после запятой
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

import fractions
f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')
