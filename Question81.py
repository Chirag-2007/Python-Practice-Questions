''' Question 8 — String Comprehension (Character Filtering)
Problem Statement
You are given a product code that may contain letters, digits, and symbols.
Write a program to create a new string containing only digits from the code.
Input Format
Single line string (product code)
Output Format
String containing only digits (0 if no digit exists)
Sample Test Case 1
Input:
AB12C3D
Output:
123
Sample Test Case 2
Input:
XYZ
Output:
0
'''

str = input()

digit = [x for x in str if x.isdigit()]
number = "".join(digit)

if len(number) != 0:
    print(number)
else:
    print("0")