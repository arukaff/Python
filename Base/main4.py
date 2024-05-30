var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 
# var1 = '5 5'
# var2 = '10 20 30 40 50'
# var3 = '10 20 30 40 50'
res=''
ls=set(var2.split(" "))&set(var3.split(" "))
ls=sorted(ls)
for i in ls:
    res+=i
    res+=' '
    
print(res)



arr = [5, 8, 6, 4, 9, 2, 7, 3]
max=int(0)
for i in range(len(arr)):
    print(arr[-i:i+3])
    # if i==0:
    #     p=arr[len(arr)-1]
    # else:
    #     p=arr[i-1]
    # if i==len(arr):
    #     n=arr[0]
    # else:
    #     p=arr[i-1]