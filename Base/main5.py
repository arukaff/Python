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

# Для заданного числа N найти количество способов его записи в виде суммы положительных чисел
# (само число N также считать одной из форм записей такой суммы, т.е. N = N  
# c=0
# num=int(input('Введите число N '))       
# s=str()
# ls=[]
# def f(n,ind):
#     global c
#     global s
#     if n==1:
#         c+=1
#         print('N равно 1, count ',c)
#         s+='+'+str(n)
#         return c
#     s=str(n)+'+'+str(ind)
#     print('Вошли ',n,s)
#     #for i in range(1,n):
#     while ind<n:
#         print('Цикл ',ind,n)
#         ind+=1
#         n-=1
#         c+=f(n,ind)
#         s+='+'+str(n)
#         c+=1
#     return c
# print(s)
# c+=f(num,0)
# for i in range(1,num):
#     s=str(num-i)
#     c+=f(i,i)
#     # c+=1
#     # s+='+'+str(i)
#     print(s)
#     s=''
#print(c)
# c=int(0)
# s=str()
# fl=0
# ls=list()
# def f(n,n1):
#    global c
#    global fl
#    global ls
#    global s
#    if n==1 or n1<0:
#        s+='+'+str(n)
#        print("Конец",n,n1,c)
#        return c
#    if fl==0:
#        print('111111',n,n1,c)
#        s=str(n)+'+'+str(n1) 
#        f(n-1,n1+1)
       
#    if n>1 and n1>0:
       
#        fl=1
#        print('22222',n,n1,c)
#        s=str(n)+'+'+str(n1)
#        f(n-1,n1) 
#    ls.append(s)
#    s=''
#    c+=1  
#    return c
# print(f(6,0))
# print(ls)
# c=int(0)
# s=str()
# fl=0
# ls=list()
# def f(n):
#     global c
#     global fl
#     global ls
#     global s
#     for i in range(1,n):
#         s=str(i)+'+'+str(n-i) 
#         if n==1:
#             s+='+'+str(n)
#             print("Конец",n,n1,c)
#             return c
#         if i>1:
#            f(i)
#         f(n-i)
#         s=str(i)+'+'+str(n-i)  
#         ls.append(s)
#         s=''
#         c+=1  
#     return c
# print(f(5))
# print(ls)
# def factorial(number):
#     if number == 1:
#         return number
#     else:
#         return number * factorial(number - 1)
# def f(n1,v):
    
#     if n1==1:
#         #s+='+'+str(1)
#         print("Конец",n1)
#         #s='+1'
#         return n1
#     else:
#         s='+'+str(n1-1)
#         print(s)
#         print('qqqqq  ',n1,v)
#         #s+='+'+str(1)
#         return f(n1-1,v)
# n=7
# c=2
# print(factorial(n+n-1)/(factorial(n)*factorial(n-1)))
# s=''
# ls=list()
# ls.append(str(n))
# ls.append(str(n-1)+'+'+str(1))
# for i in range(2,n):
#     s=str(n-i)+'+'+str(i) 
#     ls.append(s)
#     c+=1
#     s=str(n-i)
#     s+=str(f(i,n-i))
#     ls.append(s)
#     c+=1  
# print(c)
# print(ls)
# ls=list()
# s=''
# def f(n,k):
#     global s
#     if n in [0,1]:
#         print("Конец")
#         #s+='+'+str(n)
#         return n   
#     #r=f(n,k-1)+
#     print('первый вход '+str(k-n),n)
#     if k-n<=n:
#         s=str(n)+'+'+str(k-n)
#     print(s)   
#     r=f(n-1,k)
#     #s=str(k-n)
#     print('первый выход ',k,n)
#     if n > 1 and k-n>=n:
#         print('второй вход ',k,n)
#         f(n-1,n)
#         print('второй вsход ',k,n)
#     s+='+'+str(n)+'+'+str(k-n)
#     print(s)
#     return n
# print(str(f(7,7)))
# ls=list()
# s=''
# c=0
# n=5
# def f(n,k):
#     global c
#     global s
#     if n==0:
#         c+=1
#     if k ==0 or k>n:
#         print("Конец",n,k)
        
#         return  c
#     print(s)
#     s=str(n)
#     print('первый вход ',n,k) 
#     f(n,k-1)
#     #print('первый выход ',n,k)
#     #print('Второй вход ',n,k)
#     f(n-k,k)
#     #s=str(k-n)
#     print('Второй выход ',n,k)
#     s+=str(k)
#     return c
# print(str(f(n,n)))


# 
 
# lst = [12, 10, 106, 31, 15]
# sls=[]
# #d=map(int, str(lst))
# for i in lst:
#     s=str(i)
#     sum=0
#     for j in s:
#         sum+=int(j)
#     sls.append(sum)
# #d=sorted(lst, key = lambda x:(sum(map(int, str(x)),[])))
# print(sls)

