# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

input = 'a a a b c a a d c d d'
output=''
dic={}
input= input.split()
for i in input:
    if i in dic:
        output+=i+'_'+str(dic[i])+' '
    else:
        output+=i+' '
        dic[i]=0
    dic[i]=dic.get(i,0)+1
print(output)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

input = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
input=input.upper()
input=input.replace(',',' ').replace('.',' ').split()
print(len(set(input)))



# DZ

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 
# var1 = '5 5'
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'
ls=set(var2.split())&set(var3.split())
ls=sorted(ls)
for i in ls:
    print(i, end=' ')
  

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.
arr = [5, 8, 6, 4, 9, 2, 7, 3]
max=int(0)
l=len(arr)
for i in range(l):
    sum=int(arr[i-1])+int(arr[i])+int(arr[i-l+1])
    if sum>max:
        max=sum
    
print(max)