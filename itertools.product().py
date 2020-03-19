from itertools import product
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))

lst=list(product(lst1,lst2))

for i in lst:
    print(i,end=" ")
