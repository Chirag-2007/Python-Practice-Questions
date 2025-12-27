# Q21. Reverse a List In-Place (List Method)

num = list(map(int,input().split()))
reverse = num[::-1]

print(reverse)

# Q22. Unique Elements Preserving First Occurrence (Stable)

num = list(map(int,input().split()))
set_num = set(num)

print(sorted(set_num))

# Q23. Row Sums of a Matrix (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
row_sum = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    total = 0
    for j in range(0,m):
        total = total + matrix[i][j]
    row_sum.append(total)

print(row_sum)

# Q24. Column Sums of a Matrix (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
column_sum = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for j in range(0,m):
    total = 0
    for i in range(0,n):
        total = total + matrix[i][j]
    column_sum.append(total)

print(column_sum)

# Q25. Transpose Matrix (List Comprehension)

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

print(transpose)