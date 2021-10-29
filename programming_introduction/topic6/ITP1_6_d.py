n,m = map(int,input().split())
mtrx1 = [[int(0) for i in range(m)]for j in range(n)]
mtrx2 = [int(0)for i in range(m)]
mtrx = [int(0) for i in range(n)]
for i in range(n):
        mtrx1[i] = list(map(int,input().split()))
for j in range(m):
        mtrx2[j] = int(input()) 

for i in range(n):
        for j in range(m):
                mtrx[i] += mtrx1[i][j] * mtrx2[j] 
for i in range(n):
        print('%d'%(mtrx[i]))


    

