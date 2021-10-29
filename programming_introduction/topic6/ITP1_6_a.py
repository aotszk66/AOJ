n = int(input())
lst = list(map(int,input().split()))
num = int(n / 2)

for idx in range(num):
    tmp = lst[idx] 
    lst[idx] = lst[n-idx-1]
    lst[n-idx-1] = tmp

for i in range(len(lst)):
    if i != (len(lst)-1):
        print(lst[i],end=' ')
    else:
        print(lst[i])
    
