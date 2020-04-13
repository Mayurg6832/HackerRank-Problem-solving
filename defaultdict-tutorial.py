from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(list)
for i in range(n):
    s=input()
    dic[s].append(i+1)
for i in range(m):
    s=input()
    if s in dic:
        print(' '.join(map(str,dic[s])))
    else:
        print(-1)
