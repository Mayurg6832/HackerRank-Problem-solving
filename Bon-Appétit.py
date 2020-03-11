n,k=map(int,input().split())
lst=list(map(int,input().split()))
tc=int(input())
lst.pop(k)
cst=sum(lst)//2
if cst==tc:
    print("Bon Appetit")
else:
    print(abs(cst-tc))
