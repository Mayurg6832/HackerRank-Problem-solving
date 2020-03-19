from itertools import combinations
lst=[]
s,n=map(str,input().split())
s=sorted(s)
for k in range(1,int(n)+1):
    for i in combinations(s,k):
        print(''.join(i))
