n,k=map(int,input().split())
happy=0
lst=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))

for i in lst:
    if i in A:
        happy+=1
    if i in B:
        happy-=1
print(happy)
