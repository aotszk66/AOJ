import itertools

while True:
    x = 0
    n,num = map(int,(input().split()))
    if n == 0 and num == 0:
        break
    lst = [int(0) for i in range(n)]
    for i in range(n):
        lst[i] = i + 1

    for i in itertools.combinations(lst,3):
        if sum(i) == num:
            x = x + 1
    print(x)
    