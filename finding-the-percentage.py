students={}
for i in range(int(input())):
    lst=list(map(str,input().split()))
    students[lst[0]]=lst[1:]
s=input()
sum=0
for i in students[s]:
    sum+=(eval(i))

print("{0:.2f}".format(sum/len(students[s])))
