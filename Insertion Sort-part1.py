def insertion(arr):
    for i in range(1,len(arr)):
        ele=arr[i]
        j=i-1
        while j>=0 and arr[j]>ele:
            arr[j+1]=arr[j]
            print(*arr,sep=" ")
            j-=1
        arr[j+1]=ele
        
    
    return arr
n=int(input())
lst=list(map(int,input().split()))
print(*insertion(lst),sep=" ")
