from itertools import product
def check():
    mx=0
    for i in c:
        sm=sum(i)
        if sm > mx and sm <= b:
            mx=sm
    return mx

          
b,k,m=map(int,input().split())
keyb=list(map(int,input().split()))
usb=list(map(int,input().split()))
if min(keyb)+min(usb) > b:
    print(-1)
else:
    c=list(product(keyb,usb))

    print(check())
