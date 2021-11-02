while True:
    x = input()
    if x == '0':
        break
    sum = 0
    for j in range(len(x)):
        sum += int(x[j])
    print(sum)
    
