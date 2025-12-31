# Q41. Secondary Diagonal Sum (2-D Lists)

n = int(input())
matrix = []
secondary_diagonal = 0

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    secondary_diagonal = secondary_diagonal + matrix[i][n-1-i]
        
print(secondary_diagonal)

# Q42. Strict Upper Triangle Sum (2-D Lists) --> Strictly wale ma Diagonal nhi lene hote h 

n = int(input())
matrix = []
total = 0

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    for j in range(0,n):
        if i < j:
            total = total + matrix[i][j]

print(total)

# Q43. Strict Lower Triangle Sum (2-D Lists)

n = int(input())
matrix = []
total = 0

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for i in range(0,n):
    for j in range(0,n):
        if i > j:
            total = total + matrix[i][j]

print(total)

# Q44. Row with Maximum Sum (Index) (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
total_sum = []

if n == 0 or m == 0:
    print("-1")
else:
    for i in range(1,n+1):
        x = list(map(int,input().split()))
        matrix.append(x)

    for i in range(0,n):
        total = 0
        for j in range(0,m):
            total = total + matrix[i][j]
        total_sum.append(total)

    length = len(total_sum)
    max_sum = total_sum[0]
    index= 0
    for i in range(1,length):
        if max_sum < total_sum[i]:
            max_sum = total_sum[i]
            index = i
    
    print(index)

# Q45. Column with Minimum Sum (Index) (2-D Lists)

n,m = list(map(int,input().split()))
matrix = []
col_sum = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

for j in range(0,m):
    total = 0
    for i in range(0,n):
        total = total + matrix[i][j]
    col_sum.append(total)
    
min_sum = col_sum[0]
index = 0
length = len(col_sum)
for i in range(1,length):
    if min_sum > col_sum[i]:
        min_sum = col_sum[i]
        index = i
    
print(index)