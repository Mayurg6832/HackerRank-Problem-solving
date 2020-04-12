if __name__ == '__main__':
    dic={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic.keys():
            dic[score].append(name)
        else:
            dic[score]=[name]
        
    sco=sorted(dic.keys())[1]
    dic[sco].sort()
    for i in dic[sco]:
        print(i)

