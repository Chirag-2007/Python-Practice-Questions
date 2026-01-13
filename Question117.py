'''Python Coding

The national tax office is digitizing millions of account numbers. To quickly validate them, they want a system that sums up all digits of an account number.

But, as always, disruptions creep in:

• Some taxpayers accidentally enter negative account numbers.
• Some enter very long numbers beyond the standard length.
• Some even type extra characters or symbols that don’t belong.
• The system must ignore negative signs and focus only on digits.

Your task is to build a program that extracts digits and returns their sum.

Input Format
A single integer (positive or negative).

Output Format
An integer – the sum of digits.

Sample Input
1234

Sample Output
10
'''

n = input().strip()
total = 0

for i in n:
    if i.isdigit():
        total = total + int(i)

print(total)