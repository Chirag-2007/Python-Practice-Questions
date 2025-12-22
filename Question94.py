# Q1: Build & Validate a 2D Matrix, then Compute Total Sum

# n,m = list(map(int,input().split()))
# matrix = []
# total = 0
# invalid = False

# for i in range(1,n+1):
#     x = list(map(int,input().split()))
#     matrix.append(x)

# for i in range(0,n):
#     if len(matrix[i]) != m:
#         print("Invalid matrix")
#         invalid = True
#         break
#     else:
#         for j in range(0,m):
#             total = total + matrix[i][j]

# if invalid == False:
#     print(total)

# Q2: Matrix Addition with Dimension Check

# Q3: Transpose a Rectangular Matrix

# n,m = list(map(int,input().split()))
# matrix = []

# for i in range(1,n+1):
#     x = list(map(int,input().split()))
#     matrix.append(x)

# transposed_matrix = [list(column) for column in zip(*matrix)]

# for row in transposed_matrix:
#     print(*row)

# Q4: Row & Column Analytics (Max Row Sum and Max Column Sum)

# Q5: Jagged Lists — Normalize Width, Pad, and Column Sums