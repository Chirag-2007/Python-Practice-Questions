'''A student was given a task to automate the system that takes a number (n) as an input, finds the first and last digit of that number and calculates the multiplication of these two digits. The
calculated product is produced as an output by the system.
Write a code to automate this system. 
Sample Input 1 
9379 
Sample Output1 
81 
Sample Input 2 
8345 
SampleOutput2 
40 
Input Explanation: 
Input any positive number 
Output Explanation: 
Prints the product of first and last digit of a number'''

n = int(input())
num = []
length = len(str(n))

for i in range(1,length+1):
    last_digit = n % 10
    num.append(last_digit)
    n = n // 10

first = num[0]
last = num[length-1]
product = first * last
print(product)
