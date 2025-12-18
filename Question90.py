# Transpose of a Matrix -->

n,m = list(map(int,input().split()))
matrix = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

transposed_matrix = [list(column) for column in zip(*matrix)] # zip(*matrix) ya tuple deta h na ki list
print(transposed_matrix)
