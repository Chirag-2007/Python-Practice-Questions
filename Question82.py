'''Question 9 — Tuple Operations
Problem Statement
A company stores employee IDs in a tuple.
Read all IDs and print:
1.	The total count of IDs
2.	The first and last ID
Input Format
Space-separated integers.
Output Format
Three lines — count, first ID, last ID.
Sample Test Case 1
Input:
101 102 103 104
Output:
4
101
104
Sample Test Case 2
Input:
55 66
Output:
2
55
66
'''

employee = tuple(map(int,input().split()))

length = len(employee)
print(length)
print(employee[0])
print(employee[length-1])