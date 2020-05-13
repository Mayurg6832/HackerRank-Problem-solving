def find(st,to_find,R,r,C,c):
    for i in range((R-r)+1):
        for j in range((C-c)+1):
            flag=False
            for k in range(r):
                for l in range(c):
                    if st[i+k][j+l]!=to_find[k][l]:
                        flag=True
                        break
                if flag:
                    break
            if not flag:
                return True
    return False



for k in range(int(input())):
    R,C=map(int,input().split())
    st=[]
    to_find=[]
    for i in range(R):
        s=input()
        st.append(s)

    r,c=map(int,input().split())
    for i in range(r):
        s=input()
        to_find.append(s)
    
    if find(st,to_find,R,r,C,c):
        print('YES')
    else:
        print('NO')


