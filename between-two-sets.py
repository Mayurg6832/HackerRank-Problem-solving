import os

def getTotalX(a, b):
    sol=[]
    for i in range(a[-1],b[0]+1):
        lst1=[i%j for j in a]
        lst2=[j%i for j in b]
        if all(v==0 for v in lst1) and all(v==0 for v in lst2):
            sol.append(i) 
    return len(sol)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
