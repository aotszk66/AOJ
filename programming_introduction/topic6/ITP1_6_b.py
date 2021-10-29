cards = [[False for i in range(14)] for j in range(4)]
pattern = ['S','H','C','D']
x = 0
y = 0

num = int(input())
for i in range(num):
    s,n=input().split()
    n = int(n)
    for j in range(4):
        if s == pattern[j]:
            x = j
    cards[x][n] = True


for k in range(4):
    for l in range(1,14):
        if cards[k][l] == False: 
            print(pattern[k]+' '+str(l)) 
