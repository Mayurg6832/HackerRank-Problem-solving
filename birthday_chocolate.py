n=input()
count=0
s=list(map(int,input().split()))
d,m=map(int,input().split())
for i in range(len(s)):
    print(s[i:m])
    if sum(s[i:m]) == d:
        count+=1
    m+=1
print(count)
