''' Question 5 — Two-Dimensional List (Access & Storage)
Problem Statement
A cinema hall has 2 rows and 3 columns of seats.
Each number represents the seat ID.
Read the 2×3 matrix and print the middle seat ID of the second row.
Input Format
Two lines, each with three integers.
Output Format
Single integer — middle seat ID of row 2.
Sample Test Case 1
Input:
101 102 103
201 202 203
Output:
202
Sample Test Case 2
Input:
11 12 13
21 22 23
Output:
22
'''

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

arr = [row1, row2]  # bas do rows ko list me daal do
print(arr[1][1])



