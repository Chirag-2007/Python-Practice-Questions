'''Question 10 — Sets and Dictionaries
Problem Statement
Read names of students who attended two workshops.
Find the unique students (from both workshops) and store their total count in a dictionary.
Input Format
Line 1: names from Workshop 1
Line 2: names from Workshop 2
Output Format
Dictionary showing total unique students.
Sample Test Case 1
Input:
Riya Aman Neha
Aman Rahul
Output:
{'Total Students': 4}
Sample Test Case 2
Input:
A B C
C D E F
Output:
{'Total Students': 6}'''

name1 = set(input().split())
name2 = set(input().split())

union_name = name1.union(name2)
length = len(union_name)

print({'Total Students':length})
