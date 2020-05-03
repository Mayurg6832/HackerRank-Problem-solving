from collections import namedtuple

n = int(input())
columns = input().split()

mrks=0

for i in range(n):
    students=namedtuple('student',columns)
    MARKS,CLASS,NAME,ID=input().split()
    student=students(MARKS,CLASS,NAME,ID)
    mrks+=int(student.MARKS)


print('{:.2f}'.format(mrks/n))
