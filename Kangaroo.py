def func(x1,v1,x2,v2):
    for i in range(5000):
        if (x1+v1)==(x2+v2):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"


x1,v1,x2,v2=map(int,input().split())
print(func(x1,v1,x2,v2))
