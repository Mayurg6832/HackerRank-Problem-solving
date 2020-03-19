input()
lst=list(map(int,input().split()))
lst=set(lst)
input()
lst1=list(map(int,input().split()))
lst1=set(lst1)
ans=[]
for i in lst.difference(lst1):
    ans.append(i)
for i in lst1.difference(lst):
    ans.append(i)
for i in sorted(ans):
    print(i)
