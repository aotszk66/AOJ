S = int(input())
h = S / 3600
a = S % 3600
m = a / 60
s = a % 60

print('%d:%d:%d'%(h,m,s))