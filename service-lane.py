n,k=map(int,input().split())
lst=list(map(int,input().split()))
for _ in range(k):
    m,n=map(int,input().split())
    print(min(lst[m:n+1]))
