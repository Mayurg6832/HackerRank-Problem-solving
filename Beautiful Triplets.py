def beautifulTriplets(d, arr):
    n=len(arr)
    ans=0
    for i in range(n):
        if arr[i]+d in arr and arr[i]+d+d in arr:
            ans+=1
    return ans


n,d=map(int,input().split())
arr=list(map(int,input().split()))
print(beautifulTriplets(d,arr))
