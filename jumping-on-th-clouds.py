n=int(input())
clouds=list(map(int,input().split()))
count=0
i=0
while i<(len(clouds)-1):
    if i+2<len(clouds) and clouds[i+2]==0:
        count+=1
        i+=2
    else:
        count+=1
        i+=1
print(count)
