''' Question 3 — filter() Function
Problem Statement
Out of several ages entered, keep only the ages of adults (18 and above).
Input Format
Space-separated integers.
Output Format
List of ages ≥ 18.
Sample Test Case 1
Input:
12 18 25 16 30
Output:
[18, 25, 30]
Sample Test Case 2
Input:
10 11 15
Output:
[]
'''

age = list(map(int,input().split()))

age_18_more = list(filter(lambda x: x >= 18,age))
print(age_18_more)