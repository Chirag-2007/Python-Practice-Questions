'''Python Coding

A mathematician has a requirement to design a system where 
the system takes an input a number of n digits and finds out the largest digit from that number. 
The largest digit is the output.

Write a code to develop this system to fulfill his requirements.

Sample Input 1
46749   // Number

Sample Output 1
9       // largest digit in the number

Sample Input 2
386748

Sample Output 2
8

Input Explanation:
Input any number

Output Explanation:
Displays the largest digit in a given number of n digits.
'''

n = int(input())
num = []
length = len(str(n))

for i in range(1,length+1):
    last_digit = n % 10
    num.append(last_digit)
    n = n // 10

max_num = 0
for i in num:
    if max_num < i:
        max_num = i

print(max_num)

# IMPORTANT POINT-->
# length function is used in str if we use in int then error will occur...