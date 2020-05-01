import math
s=input()
ans=[]
s=s.replace(" ","")
ln=len(s)**(1/2)
n=math.floor(ln)
m=math.ceil(ln)
o=m
j=0
l=len(s)
if n*m<l:
    n=m
for i in range(n+1):
    ans.append(s[j:m])
    j=m
    m+=o
encryp=''
for i in range(m):
    for j in range(n+1):
        if i<len(ans[j]):
            encryp+=ans[j][i]
    encryp+=" "

print(encryp)
