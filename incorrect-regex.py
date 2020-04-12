import re
for i in range(int(input())):
    n=input()
    try:
        re.compile(n)
        print(True)
    except Exception:
        print(False)
