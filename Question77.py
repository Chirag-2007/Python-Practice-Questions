''' Question 4 — reduce() Function
Problem Statement
Sum the daily steps walked in a week and print the total.
Input Format
Space-separated integers (steps per day).
Output Format
Total steps in the week.
Sample Test Case 1
Input:
3000 4000 3500 5000 4200 3900 4500
Output:
28100
Sample Test Case 2
Input:
1000 1000 1000 1000 1000 1000 1000
Output:
7000
'''
from functools import reduce # reduce function chalane ke liya import karna padta h

steps = list(map(int,input().split()))

total = reduce(lambda x,y:x + y,steps)
print(total)