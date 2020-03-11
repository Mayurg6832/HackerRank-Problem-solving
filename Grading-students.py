#!/bin/python3

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    if grades < 38:
        print(grades)
    elif grades%5==0:
        print(grades)
    else:
        if (5*((grades//5)+1))-grades < 3:
            print(5*((grades//5)+1))
        else:
            print(grades)

for i in range(int(input())):
    gradingStudents(int(input()))
