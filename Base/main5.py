# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
inp = 7 #int(input ('Введите число N '))
def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1)+fib(n-2)
print(fib(5))


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
ls='1 3 3 3 4'.split()
def minmax(list):
    re=[list[0],list[0]]
    for i in list:
        if re[0]>i:
            re[0]=i
        if re[1]<i:
            re[1]=i
    return re
m=minmax(ls)
for i in range(len(ls)):
    if ls[i] == m[1]:
        ls[i]=m[0]
print(ls)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 
inp =5# int(input ('Введите число N '))
def simple(n):
    d=[2,3,5]
    if n==1 or n in d:
        return 'yes'
    for i in d:
        if n%i==0:
            return 'no'
    return 'yes'
print(simple(inp))

# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
def lastchr(s):
    if len(s)<1:
        return ''
    print(s[-1], end='')
    lastchr(s[:-1])
s='3 4' #input ('Введите число строку: ')
lastchr(s)
print('')

#определить является ли слово полиндромом
def poliyes(b):
    if b[0]!=b[-1]:
        return "no"
    elif len(b)<=1:
        return "yes"
    return poliyes(b[1:-1])
print(poliyes('weww'))


#DZ

# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def st(a,b):
    if b==0:
        return 1
    return a*st(a,b-1)
print(st(3,5))

#способ 2
a=3
b=5
res=a
for i in range(b-1):
    res*=a
print(res)

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
def sum(a,b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)
    
print(sum(-1,-2))



