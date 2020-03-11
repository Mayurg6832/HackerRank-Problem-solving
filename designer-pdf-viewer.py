lst=list(map(int,input().split()))
s=input()
f=0
for i in s:
    if lst[ord(i)-97]>f:
        f=lst[ord(i)-97]
print(len(s)*f)
