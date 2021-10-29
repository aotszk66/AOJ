a,b,c = map(int,input().split())
if a <= b and b <= c:
    print('%d %d %d'%(a,b,c))
elif a <= c and c <= b:
    print('%d %d %d'%(a,c,b))
elif b <= a and a <= c:
    print('%d %d %d'%(b,a,c))
elif b <= c and c <= a:
    print('%d %d %d'%(b,c,a))
elif a <= b and c <= a:
    print('%d %d %d'%(c,a,b))
elif c <= b and b <= a:
    print('%d %d %d'%(c,b,a))