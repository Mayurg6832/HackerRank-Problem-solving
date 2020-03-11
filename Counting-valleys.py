n=int(input())
steps=input()
valley=0
level=0
for step in steps:
    if step=="U":
        level+=1
        if level==0:
            valley+=1
    else:
        level-=1
print(valley)
