from itertools import combinations_with_replacement

s,n=map(str,input().split())
s=sorted(s)
for i in combinations_with_replacement(s,int(n)):
    print(''.join(i))
