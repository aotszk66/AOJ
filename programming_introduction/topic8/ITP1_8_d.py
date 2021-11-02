str = ''
s = input()
p = input()
num = len(s) * 2 - 1
lst = ['0']*num
idx = 0

for i in range(len(s)):
    lst[i] = s[i]
for j in range(len(s),num):
    lst[j] = s[idx]
    idx += 1

for k in range(len(lst)):
    str = str + lst[k]

if (p in str) == True:
    print('Yes')
else:
    print('No')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # idx = 0
    # num = s.rfind(p[0]) #文字列sの逆からpの頭文字のインデックスを検索
    # n  = num  + len(s) 
    # for i in range(num,n):
    #     if i > len(s) - 1:  #sの文字列の末尾まで来たら，先頭の文字からlst代入するように
    #         lst[i] = s[idx]
    #         idx += 1
    #     elif i <= len(s) - 1:
    #         lst[i] = s[i] 
            
    # for j in range(len(lst)):
    #     if lst[j] != '0':
    #         str = str + lst[j]
    # if str in p:
    #     print('Yes')
    # else:
    #     print('No')
