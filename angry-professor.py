for i in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    count=0
    for i in lst:
        if i <= 0:
            count+=1
    if count >=k:
        print("NO")
    else:
        print("YES")
