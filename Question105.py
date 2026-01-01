# Q46. Rotate 90° Clockwise (2-D Lists)

n,m = list(map(int, input().split()))

matrix = []
for i in range(1,n+1):
    x = list(map(int, input().split()))
    matrix.append(x)

transpose = []
for j in range(0,m):
    row = []
    for i in range(0,n):
        row.append(matrix[i][j])
    transpose.append(row)

for i in range(0,m):
    transpose[i].reverse()
print(transpose)

# Q47. Border Sum (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
total = 0

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    for j in range(0,m):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            total = total + matrix[i][j]
print(total)

# Q48. Matrix Search (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
total = 0

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)
num = int(input())

num_found = False
for i in range(0,n):
    for j in range(0,m):
        if matrix[i][j] == num:
            num_found = True

if num_found == True:
    print("Found")
else:
    print("NotFound")

# Q49. Jagged Row Sums (Jagged Lists)

n = int(input())
matrix = []
row_sum = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    total = 0
    length = len(matrix[i])
    for j in range(0,length):
        total = total + matrix[i][j]
    row_sum.append(total)
print(row_sum)

# Q50. Flatten Jagged → Sorted Unique (Jagged + Set)

n = int(input())
matrix = []
num = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    length = len(matrix[i])
    for j in range(0,length):
        num.append(matrix[i][j])

set_num = set(num)
print(list(sorted(set_num)))