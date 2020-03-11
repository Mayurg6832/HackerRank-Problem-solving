lst=[]
ltor=0
rtol=0
n=int(input())
for i in range(n):
    lst.append(list(map(int,input().split())))
for i in range(n):
    ltor+=lst[i][i]

j=0
for i in range(n-1,-1,-1):
    rtol+=lst[i][j]
    j+=1

print(abs(ltor-rtol))
