from itertools import permutations

s,n=map(str,input().split())

lst=list(permutations(s,int(n)))
lst.sort()
for i in lst:
    for k in i:
        print(k,end="")
    print()
