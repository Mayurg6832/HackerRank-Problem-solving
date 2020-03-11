if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx=max(arr)
    arr[:]=(i for i in arr if i!=mx)
    print(max(arr))
