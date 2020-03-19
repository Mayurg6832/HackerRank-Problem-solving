s=input()
ans=[]
i=0
j=1
c=1
if len(s)==1:
    print((1,int(s)))
while j!=len(s):
    if s[i]==s[j]:
        c+=1
        i+=1
        j+=1    
        if i==len(s)-1 and j==len(s):
            ans.append((c,int(s[i])))
    else:
        ans.append((c,int(s[i])))
        i+=1
        j+=1
        c=1
        if j==len(s):
            ans.append((c,int(s[j-1])))

for i in ans:
    print(i,end=" ")
