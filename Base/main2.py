"""
Задача №9. Общее обсуждение
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
"""
#n= int(input("Введите размер факториала"))
#f=int(1)
#while n>0:
#   f*=n
#   n=n-1
#print(f)


"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.


a= int(input("Введите число А"))
n=int(2)
last =0
cur = 1
while cur<a:
    last,cur=cur, last+cur
    n+=1
if a !=cur:
    n=-1
print(n)
"""


"""
Задача №11.

o=int(0)
oo=int(0)
n= int(input("Введите общее колличество дней"))
for i in range(n):
    if int(input("Введите температуру дня № "+ str(i+1)))>0:
        o+=1
    else:
        o=0
    if o>oo:
        oo=o
print(oo)
"""
"""
Задача №13.
n= int(input("Введите общее колличество арбузов"))
max=0
min=0
for i in range(n):
    w= int(input("Введите вес арбуза № "+ str(i+1)))
    if w>max:
        max=w
    elif w<min:
        min=w
print(max,min)
"""
#DZ

"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

o=int(0)
oo=int(0)
n= int(input("Введите колличество монеток"))
for i in range(n):
    if int(input("Введите сторону(1 или 0) монеты № "+ str(i+1)))>0:
        o+=1
    else:
        oo+=1
if oo>o:    
    print(o)
else:
    print(oo)
"""
"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

s= int(input("Введите сумму чисел"))
p= int(input("Введите произведение чисел"))
i=0
while i <1000:
    if (s-i)*i==p:
        print(i,s-i)
        i=1000
    i+=1
"""
"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
"""
n= int(input("Введите N"))
i=0
while 2**i <n:
    print(2**i)
    i+=1