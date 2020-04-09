n=int(input())
grid=[[x for x in input()] for i in range(n)]

for i in range(1,n-1):
    for j in range(1,n-1):
        if grid[i][j]>grid[i][j-1] and grid[i][j]>grid[i][j+1] and grid[i][j]>grid[i-1][j] and grid[i][j]>grid[i+1][j]:
                grid[i][j]="X"

for i in range(n):
    print(''.join(str(x) for x in grid[i]))
