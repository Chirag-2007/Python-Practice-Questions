'''Q11. Main Diagonal Sum (2-D Lists)
Problem (Bloom: Understand→Apply):
For a square matrix n×n, print the sum of main diagonal elements.
Input
Line 1: int n
Next n lines: n ints each
Output
Single int
Sample 1
Input
2
1 2
3 4
Output
5
Sample 2
Input
3
1 0 1
0 1 0
1 0 1
Output
3'''
arr_number = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total = 0
length = len(arr_number)

for i in range(0,length):
    for j in range(0,length):
        if i == j:
            total = total + arr_number[i][j]
print(total)