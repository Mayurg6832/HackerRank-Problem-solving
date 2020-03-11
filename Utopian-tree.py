for i in range(int(input())):
    num=int(input())
    flag=0
    height=0
    if num==0:
        print(1)
    else:
        for k in range(num+1):
            if flag==0:
                height+=1
                flag=not flag
            elif flag==1:
                height*=2
                flag=not flag
        print(height)
