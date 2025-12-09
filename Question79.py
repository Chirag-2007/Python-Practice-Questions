'''Question 6 — Jagged List (Unequal Rows)
Problem Statement
A teacher stores marks of students from two classes in separate lists.
Class A has 3 students, and Class B has 2.
Create a jagged list to store both and print the total number of students across both classes.
Input Format
Two lines —
Line 1: marks of Class A (space-separated)
Line 2: marks of Class B (space-separated)
Output Format
Single integer — total number of students.
Sample Test Case 1
Input:
80 90 75
60 85
Output:
5
Sample Test Case 2
Input:
45 55
70 65 80 90
Output:
6
'''

row1 = list(map(int,input().split()))
row2 = list(map(int,input().split()))

jag_arr = [row1,row2]
total = len(row1) + len(row2)
print(total)
