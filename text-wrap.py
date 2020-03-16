import textwrap

def wrap(string, max_width):
    lst=textwrap.wrap(string,max_width)
    for i in range(len(lst)-1):
        print(lst[i])
    return lst[-1]
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
