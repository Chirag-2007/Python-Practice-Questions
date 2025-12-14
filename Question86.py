'''Question 6
Question Preview
Coding
Electricity Bill Calculator
Testcase: 6
Description:
Write a program to calculate and display the total electricity bill for N households.
Rules:
•	First 100 units → ₹5/unit
•	Next 100 units → ₹7/unit
•	Beyond 200 units → ₹10/unit
Store each household’s total bill in a dictionary and print it.
Input Format:
•	First line: integer N
•	Next N lines: <house_name> <units_consumed>
Output Format:
•	Dictionary {house_name: bill_amount}
Sample Test Case:
Input
3
AgarwalHouse 80
MehtaHouse 150
SharmaVilla 220
Output
{'AgarwalHouse': 400, 'MehtaHouse': 950, 'SharmaVilla': 1400}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    name_bill = input().split()
    name = name_bill[0]
    bill = int(name_bill[1])
    if bill <= 100:
        total = bill * 5
    elif bill > 100 and bill <= 200:
        total = 100*5 +(bill - 100)*7
    else:
        total = 100*5 + 100*7 + (bill - 200)*10
    emp_dict[name] = total
print(emp_dict)