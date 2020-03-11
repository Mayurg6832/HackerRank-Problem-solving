for i in range(int(input())):
    x,y,z=map(int,input().split())
    cata,catb=abs(x-z),abs(y-z)
    if cata == catb:
        print("Mouse C")
    elif cata>catb:
        print("Cat B")
    else:
        print("Cat A")
