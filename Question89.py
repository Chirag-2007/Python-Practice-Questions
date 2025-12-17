'''Question 9
Class Topper Finder
Description:
Read names of N students with their marks.
Find and print the student who scored the highest marks in {name: marks} format.
Input Format:
•	First line: integer N
•	Next N lines: <student_name> <marks>
Output Format:
•	Dictionary with topper {name: marks}
Sample Test Case:
Input
4
Ravi 75
Meena 89
Arjun 67
Neha 93
Output
{'Neha': 93}'''

n = int(input())
emp_dict = {}
max_marks = 0
topper_name = ''

for i in range(1,n+1):
    data = input().split()
    name = data[0]
    marks = int(data[1])
    if marks > max_marks:
        max_marks = marks
        topper_name = name
print({topper_name:max_marks})