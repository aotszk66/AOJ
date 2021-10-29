rooms = [[[int(0) for j in range(10)]for j in range(3)]for k in range(4)]

num = int(input())
for l in range(num):
    b,f,r,v = map(int,(input().split()))
    rooms[b-1][f-1][r-1] += v
    if rooms[b-1][f-1][r-1] < 0:
        rooms = [b-1][f-1][r-1] = 0

for i in range(4):
    for j in range(3):
        for k in range(10):
            print('',end=' ')
            print(rooms[i][j][k],end='')
        print('',end='\n')
    if i != 3:
        print('#'*20)
    
        
 