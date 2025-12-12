'''Question 3
Question Preview
Coding
Student Attendance Manager
Testcase: 6
Description:
At City High School, attendance for 5 days is recorded for each student.
Store attendance as a tuple (P for present, A for absent) in a dictionary with the student’s name as key.
Then print the number of days each student was present in {name: present_count} format.
Input Format:
•	First line: integer N
•	Next N lines: student name followed by 5 attendance entries (P or A)
Output Format:
•	Dictionary {student_name: present_count}
Sample Test Case:
Input
2
Rohit P A P P A
Tina P P P P P
Output
{'Rohit': 3, 'Tina': 5}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    data = input().split()
    name = data[0]
    attendence = data[1:]
    count_present = 0
    for i in attendence:
        if "P" == i:
            count_present = count_present + 1
    emp_dict[name] = count_present
print(emp_dict)