s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apple=list(map(int,input().split()))
orange=list(map(int,input().split()))
countA=0
countO=0
for i in range(len(apple)):
    temp=a+apple[i]
    if temp in range(s,t+1):
        countA+=1

for i in range(len(orange)):
    temp=b+orange[i]
    if temp in range(s,t+1):
        countO+=1
print(countA)
print(countO)
