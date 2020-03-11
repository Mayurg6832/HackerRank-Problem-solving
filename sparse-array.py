lst=[]
lst1=[]
ins=int(input())
for i in range(ins):
    lst.append(input())
qs=int(input())
for _ in range(qs):
    lst1.append(input())
for i in lst1:
    print(lst.count(i))
