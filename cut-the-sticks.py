def cutTheSticks(arr):
    while len(arr)>0:
        arr=[i-min(arr) for i in arr]
        print(len(arr))
        arr=[i for i in arr if i!=0]

input()
lst=list(map(int,input().split()))
cutTheSticks(lst)
