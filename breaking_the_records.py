n=input()
scores=list(map(int,input().split()))
lowest=scores[0]
highest=scores[0]
low_count=0  #not consider 1st element 
high_count=0 
for i in scores:
    if i > highest:
        highest=i
        high_count+=1

for i in scores:
    if i < lowest:
        lowest=i
        low_count+=1

print(high_count,low_count)
