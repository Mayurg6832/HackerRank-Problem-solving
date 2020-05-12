def stones(n, a, b):
    o=b-a
    ans=[(n-1)*a]
    p=0
    while ans[-1]!=((n-1)*b):
        p=o+ans[-1]
        ans.append(p)
    
    ans.sort()
    for i in ans:
        print(i,end=" ")


for i in range(int(input())):
    n=int(input())
    a=int(input())
    b=int(input())
    stones(n,a,b)
    print()
