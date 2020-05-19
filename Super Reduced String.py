def reduce_string(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return ''.join(stack)
    return 'Empty String'

print(reduce_string(input()))
