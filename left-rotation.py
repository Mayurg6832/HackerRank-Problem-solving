n,d=map(int,input().split())
lst=list(map(int,input().split()))
d%=len(lst)
for i in ((lst[d:]+lst[:d])):
    print(i,end=" ")
