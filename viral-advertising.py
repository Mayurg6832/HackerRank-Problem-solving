n=int(input())
people=5
liked=0
for i in range(n):
    liked+=(people//2)
    people=(people//2)
    people*=3
print(liked)
