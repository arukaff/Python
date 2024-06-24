# Для заданного числа N найти количество способов его записи в виде суммы положительных чисел
# (само число N также считать одной из форм записей такой суммы, т.е. N = N  
# 
# c=0
# def f(n,k):
#     global c
#     if n==0 and k==0:
#         c+=1
#         return 1
#     if n>0 and k==0:
#         return 0
#     if n>=k:
#         f(n,k-1)+f(n-k,k)
#     if k>n:
#         f(n,n)
#     return c
# n=int(input('Введите число N: '))
# print('Количество способов разложения числа N: ',f(n,n))

#без рекурсии
n=10
i=0
ls=[]
k=n
while k>0:
    s=[0 for i in range(n+1)]
    s[0]=k
    for i in range(1,n+1):
        s[i]=n-sum(s)
        if s[i]==0 and s[0:-1] not in ls:
            if s[i-1]<=s[0]:
                ls.append(s[0:-1])
                for j in range(1,i):
                    if s[j]>1:
                        s[j]-=1
                        s.insert(j+1,1)
                        del s[-1]
                        break
            else:
                s[i]=s[i-1]-s[0]
                s[i-1]=s[0]
    k-=1
print(ls)
print(len(ls))