alice=list(map(int,input().split()))
bob=list(map(int,input().split()))
alice_total=0
bob_total=0
for i in range(len(alice)):
    if alice[i]>bob[i]:
        alice_total+=1
    elif alice[i]<bob[i]:
        bob_total+=1
    else:
        pass

print(alice_total,bob_total)
