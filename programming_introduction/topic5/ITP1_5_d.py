n = int(input())
i = 1
x = 0
y = 0
print(' ',end='')
while i <= n:
    x = i
    if int(x % 3) == 0:
        print(i,end=' ')
        x = 0
    if int(x % 10) == 3:
        print(i,end=' ')
        x = 0
    while x != 0:
        x = int(x / 10)
        if x:
            if int(x % 10) == 3:
                print(i,end=' ')  
                x = 0  
    i = i + 1
    