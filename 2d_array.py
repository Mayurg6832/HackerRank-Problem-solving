arr=[]
for i in range(6):
    arr.append(list(map(int,input().split())))
count=[]
for i in range(4):
    for j in range(4):
        count.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

print(max(count))
