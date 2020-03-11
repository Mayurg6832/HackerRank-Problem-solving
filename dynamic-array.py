seqlist=[]
lastAnswer=0
n,q=map(int,input().split())
for _ in range(n):
    seqlist.append([])
for i in range(q):
    p,x,y=map(int,input().split())
    if p==1:
        seqlist[(x^lastAnswer)%n].append(y)
    else:
        lastAnswer=seqlist[(x^lastAnswer)%n][y%(len(seqlist[(x^lastAnswer)%n]))]
        print(lastAnswer)
        
