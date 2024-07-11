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

#без рекурсии считает и разписывает правильно только до 10
# n=10
# ls=[]
# k=n
# while k>0:
#     s=[0 for i in range(n+2)]
#     s[0]=k
#     for i in range(1,n+2):
#         s[i]=n-sum(s)
#         if s[i]==0 and s[0:-2] not in ls:
#             if s[i-1]<=s[0]:
#                 ls.append(s[0:-2])
#                 for j in range(s.index(0),0,-1):
#                     if s[j]>1:
#                         s[j]-=1
#                         if s[j]>s[j+1]:
#                             s[j+1]+=1
#                             e=s.index(0)-(j+1)
#                             su=sum(s[e:])
#                             if s[j]>=su:
#                                 s[e]=su
#                                 s[e+1:]=map(lambda x: x*0,s[e+1:])
#                         else:
#                             s.insert(j+1,1)
#                             del s[-1]
#                         break
#             else:
#                 s[i]=s[i-1]-s[0]
#                 s[i-1]=s[0]
#     k-=1
# print(len(ls))
# for i in ls:
#     print(i)


n=10
ls=[]
k=n

while k>0:
    s=[0 for i in range(n+2)]
    s[0]=k
    i=0
    r=True
    for i in range(1,n+2):
        #i=s.index(0)
        s[i]=n-sum(s)
        if s[i]==0 and s[0:-2] not in ls:
            if s[i-1]<=s[0]:
                ls.append(s[0:-2])
                for j in range(i,0,-1):
                    if s[j]>1:
                        s[j]-=1
                        if s[j]>s[j+1]:
                            s[j+1]+=1
                            s[j+2:]=map(lambda x: x*0,s[j+2:])
                        else:
                            s.insert(j+1,1)
                            del s[-1]
                        break
            else:
                s[i]=s[i-1]-s[0]
                s[i-1]=s[0]
        
    k-=1
print(len(ls))
for i in ls:
    print(i)