''' Question 1 — List Comprehension
Problem Statement
A teacher records the marks of students in a test.
From a list of marks, create a new list containing only marks greater than or equal to 50 (students who passed).
Input Format
One line with space-separated integers.
Output Format
List of marks ≥ 50.
Sample Test Case 1
Input:
45 60 70 38 92
Output:
[60, 70, 92]
Sample Test Case 2
Input:
10 20 30
Output:
[]'''

marks = list(map(int,input().split()))

marks_50_more = [x for x in marks if x >= 50]
print(marks_50_more)