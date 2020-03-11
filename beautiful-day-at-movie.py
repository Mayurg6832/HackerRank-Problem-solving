i,j,k=map(int,input().split())
count=0
for i in range(i,j+1):
    revi=int(str(i)[::-1])
    if (abs(i-revi)/k).is_integer():
        count+=1
print(count)
