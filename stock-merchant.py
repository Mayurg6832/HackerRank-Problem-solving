
n=int(input())
lst=list(map(int,input().split()))
count=0
values={i:lst.count(i) for i in lst}
for j in values.values():
    count+=(j//2)
print(count)
