'''Q 3. Problem Statement
Suppose, you are working on a grid-based game where a player collects treasure in a 2D matrix. The matrix represents the game grid, where each cell contains a certain number of coins. Your task is to calculate the sum of the elements (coins) on the borders of the matrix. The border elements are those that are in the first row, last row, first column, and last column of the matrix.
Input Format:
The first line contains two integers N and M, representing the number of rows and columns in the matrix.
The next N lines contain M integers each, representing the elements of the matrix.
Output Format:
Print a single integer, the sum of the border elements of the matrix.
Code Constraints:
•	2≤N, M≤100
•	Matrix elements are integers between -1000 and 1000.
Sample Testcase 1
Input: 
4 4
3 5 6 7
1 3 5 7
7 6 3 1
9 7 8 6
Output: 
67
Explanation:
The border elements are 3,5,6,7,7,1,6,8,7,9,7,1 and their sum is 67.'''

n, m = map(int, input().split())
arr_2d = []

for i in range(n):
    row = list(map(int, input().split()))
    arr_2d.append(row)

total = 0

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            total = total + arr_2d[i][j]
print(total)

