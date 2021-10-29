n = int(input())
lst = [int(0) for i in range(n)]
a = list(map(int,input().split()))

for i in range(n):
    lst[i] = a[i]

maximum = max(lst)
minimum = min(lst)
s = sum(lst)

print('%d %d %d'%(minimum,maximum,s))