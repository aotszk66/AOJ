import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = [0]*26
# print(type(lst[1]))

str = sys.stdin.read()

for i in str:
    idx = 0
    for j in alphabet:
        if i == j or i == j.upper():
            lst[idx] += 1
            break
        idx += 1

for k in range(len(alphabet)):
    print('%s : %d'%(alphabet[k],lst[k]))