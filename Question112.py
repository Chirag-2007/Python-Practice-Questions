# Q21. Even Squares List (List Comprehension)

n = int(input())
num = list(map(int,input().split()))

even_num = [x for x in num if x % 2 == 0]
square_num = [x*x for x in even_num]

for i in square_num:
    print(i,end=" ")

# Q22. Celsius to Fahrenheit (map with Lambda)

n = int(input())
num = list(map(int,input().split()))

fahrenheit = list(map(lambda x: int((x * 9/5) + 32),num))
print(*fahrenheit)  # * is used to print the terms in one line with space

# Q23. Total Sales Using map, filter, and reduce

from functools import reduce

n = int(input())
num = list(map(int,input().split()))

more_100 = list(filter(lambda x: x > 100,num))
total = reduce(lambda x,y: x + y,more_100)

if len(more_100) > 0:
    print(total)
else:
    total = 0
    print(total)

# Q24. Row-wise Sum of a Matrix (2D List)

n,m = map(int,input().split())
matrix = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    total = 0
    for j in range(0,m):
        total = total + matrix[i][j]
    print(total)

# Q25. Jagged List Row Lengths

n = int(input())
jag_list = []

for i in range(1,n+1):
    m = int(input())
    x = list(map(int,input().split()))
    jag_list.append(x)

for i in jag_list:
    length = len(i)
    print(length)