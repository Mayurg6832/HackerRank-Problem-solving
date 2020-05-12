def lexi(s):
    n=len(s)
    s=list(s)
    ind=0
    for j in range(n-1,0,-1):
        if s[j]>s[j-1]:
            ind=j
            break
    if ind==0:
        return 'no answer'
    frst_smll_char=s[ind-1]
    frst_smll_ind=ind-1
    nxt_smll=ind

    for j in range(ind+1,n):
        if s[j]>frst_smll_char and s[j]<s[nxt_smll]:
            nxt_smll=j
    
    s[nxt_smll],s[frst_smll_ind]=s[frst_smll_ind],s[nxt_smll]
    
    s=s[:ind]+sorted(s[ind:])
    return s
    

for i in range(int(input())):
    s=input()
    print("".join(lexi(s)))
