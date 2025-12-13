'''Question 4
Question Preview
Coding
Store Discount Evaluator
Testcase: 6
Description:
A store gives discounts based on total shopping amount.
If amount ≥ 5000 → “Gold”
If 3000 ≤ amount < 5000 → “Silver”
Else → “Regular”
Read the names and total bills of N customers and print {name: category}.
Input Format:
•	First line: integer N
•	Next N lines: <name> <amount>
Output Format:
•	Dictionary {customer_name: category}
Sample Test Case:
Input
3
Amit 2500
Neha 4500
Ravi 5200
Output
{'Amit': 'Regular', 'Neha': 'Silver', 'Ravi': 'Gold'}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    name_amount = input().split()
    name = name_amount[0]
    amount = int(name_amount[1])
    if amount >= 5000:
        title = "Gold"
    elif amount >= 3000 and amount < 5000:
        title = "Silver"
    else:
        title = "Regular"
    emp_dict[name] = title
print(emp_dict)