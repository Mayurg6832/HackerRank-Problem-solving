n,k=map(int,input().split())
lst=list(map(int,input().split()))
lst2=[]
lst3=[]
for i in lst:
    for j in range(1,i+1):
        if len(lst2)==k:
            lst3.append(list(lst2[:]))
            lst2.clear()
            lst2.append(j)
        else:
            lst2.append(j)
        
    lst3.append(list(lst2[:]))
    lst2.clear()

count=0        
for i in range(len(lst3)):
    if (i+1) in lst3[i]:
        count+=1
print(count)
