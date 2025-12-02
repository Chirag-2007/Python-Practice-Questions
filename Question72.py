'''Question 1
Employee Salary Manager
Description:
Store each employee’s monthly salary for three months as a tuple in a dictionary, using the employee’s name as key. Then compute the total salary paid for each employee and print {name: total_salary}.
Input Format:
•	First line: integer N
•	Next N lines: employee name followed by three integer salaries
Output Format:
•	Dictionary {employee_name: total_salary}
Sample Test Case:
Input
2
Ravi 25000 27000 26000    #Ravi,25k,27k,26k
Meena 30000 31000 29500
Output
{'Ravi': 78000, 'Meena': 90500}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    name_salary = input().split()
    name = name_salary[0]
    salary = tuple(map(int,name_salary[1:]))
    total = 0
    for i in salary:
        total = total + i
    emp_dict[name] = total # dictionary ki form ma likhne ka tarika

print(emp_dict)
    

