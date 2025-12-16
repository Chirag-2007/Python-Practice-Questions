'''Question 8
Question Preview
Coding
Cafeteria Menu Tracker
Testcase: 6
Description:
Read N menu items and their calorie counts.
Display only those items whose calories are greater than or equal to 300 in a dictionary.
Input Format:
•	First line: integer N
•	Next N lines: <item_name> <calories>
Output Format:
•	Dictionary of items with calories ≥ 300
Sample Test Case:
Input
4
Sandwich 250
Burger 350
Salad 150
Pizza 400
Output
{'Burger': 350, 'Pizza': 400}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    food = input().split()
    name = food[0]
    calories = int(food[1])
    if calories >= 300:
        emp_dict[name] = calories
print(emp_dict)
