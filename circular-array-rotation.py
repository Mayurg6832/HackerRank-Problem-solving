def rotate(lst,k):
    lst=lst[-k:]+lst[:-k]
    for i in query:
        print(lst[i])


n,k,q=map(int,input().split())
query=[]
lst=list(map(int,input().split()))
for i in range(q):
    query.append(int(input()))
if k==n:
    for i in query:
        print(lst[i])
elif k>n:
    k%=n
    rotate(lst,k)
else:
    rotate(lst,k)
