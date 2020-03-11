input()
dic={}
birds=list(map(int,input().split()))
for i in range(1,6):
    dic[i]=birds.count(i)
count=0
l=0
largest=0
allb=[]
for i in range(1,6):
    if dic[i] > l:
        count+=1
        largest=i
        l=dic[i]
        if count > 1:
            allb.append(largest)
if count == 1:
    print(largest)
else:
    print(max(allb))
