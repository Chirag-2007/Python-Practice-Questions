'''Compute the Gross Salary

A company has a policy of providing perks to its executives. The company has divided the executives into four levels. The levels and their corresponding perks are shown below:

Level	Conveyance Allowance	Entertainment Allowance
1	        1000	                    500
2	        750	                        200
3	        500	                        100
4	        250	                          0

An executive’s gross salary includes:

Basic Pay

House Rent Allowance (HRA) which is 25% of basic pay

Other perks based on the executive’s level

Your Task:

Write a program that reads an executive’s level number and basic pay, and then computes the gross salary.

Input Format:

First line: Level number (integer)

Second line: Basic pay (integer)

Output Format:

Print the gross salary'''

level = int(input())
basic_pay = int(input())

if level == 1:
    conveyance = 1000
    entertainment = 500
elif level == 2:
    conveyance = 750
    entertainment = 200
elif level == 3:
    conveyance = 500
    entertainment = 100
elif level == 4:
    conveyance = 250
    entertainment = 0
else:
    conveyance = 0
    entertainment = 0

hra = 0.25 * basic_pay
gross = basic_pay + hra + conveyance + entertainment

print(f"{gross:.6f}")
