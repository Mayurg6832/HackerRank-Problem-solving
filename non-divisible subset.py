n,k=map(int,input().split())
lst=list(map(int,input().split()))

freq=[0 for i in range(k)]

for i in lst:
    freq[i%k]+=1

if k%2==0:
    freq[k//2]=min(freq[k//2],1)

ans=min(freq[0],1)

for i in range(1,(k//2)+1):
    ans+=max(freq[i],freq[k-i])

print(ans)
