n,m=map(int,input().split())
lst=[0]*(n+2)
for _ in range(m):
    a,b,k=map(int,input().split())
    lst[a]+=k
    lst[b+1]-=k

sm=0
mx=0
for i in range(len(lst)):
    sm+=lst[i]
    mx=max(sm,mx)

print(mx)

