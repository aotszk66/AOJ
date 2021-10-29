while True:
    a,op,b = input().split()
    a, b = int(a), int(b)
    op = str(op)
    if op == '?':
        break
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b 

    print('%d'%(result))
