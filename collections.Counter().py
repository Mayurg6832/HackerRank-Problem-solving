from collections import Counter
x=input()
cost=0
shoes = list(map(int,input().split()))
shoes_count= Counter(shoes)
n=int(input())
for i in range(n):
    shoes_size,price=map(int,input().split())
    if shoes_size in shoes_count.keys() and shoes_count[shoes_size] > 0:
        cost+=price
        shoes_count[shoes_size]-=1
print(cost)
