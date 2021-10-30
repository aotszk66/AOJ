r,c = map(int,input().split())
mtrx = [[int(0) for i in range(c+1)] for j in range(r+1)]

for i in range(r):
    lst = list(map(int,input().split()))
    for j in range(c):
        mtrx[i][j] = lst[j]
    
for x in range(r):
    for y in range(c):
        mtrx[x][c] += mtrx[x][y]

for x in range(c):
    for y in range(r):
        mtrx[r][x] += mtrx[y][x]

for k in range(c):
    mtrx[r][c] += mtrx[r][k]


for a in range(r+1):
    for b in range(c+1):
        if b == c:
            print('%d'%(mtrx[a][b]),end='')
        else:
            print('%d'%(mtrx[a][b]),end=' ')
        
    print()