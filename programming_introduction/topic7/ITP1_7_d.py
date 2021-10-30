n,m,l = map(int,input().split())

mtrx1 = [[int(0) for i in range(m)] for j in range(n)]
mtrx2 = [[int(0) for i in range(l)] for j in range(m)]
sum = [[int(0) for i in  range(l)] for j in range(n)]

for x in range(n):
    lst = list(map(int,input().split()))
    mtrx1[x] = lst

for y in range(m):
    lst2 = list(map(int,input().split()))
    mtrx2[y] = lst2

for i in range(l):
    for j in range(n):
        for k in range(m):
            sum[j][i] += mtrx1[j][k] * mtrx2[k][i]

for a in range(n):
    for b in range(l):
        if b == l-1:
            print('%d'%(sum[a][b]),end='')
        else:
            print('%d'%(sum[a][b]),end=' ') 

    print()