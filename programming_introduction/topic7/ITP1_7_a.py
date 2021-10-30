while True:
    m,f,r = map(int,input().split())
    if m == -1 and f == -1 and r == -1:
        break
    
    score = m + f

    if m == -1 or f == -1:
        print('F')
    elif score >= 80:
        print('A')
    elif score >= 65 and score < 80:
        print('B')
    elif score >= 50 and score < 65:
        print('C')
    elif score >= 30 and score < 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    elif score < 30:
        print('F')
