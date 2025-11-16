'''1. Problem Statement1 : Greatest Common divisor of two integers 
Write a Python program to print positive numbers in a List using if and while list. The list 
should be created by taking input from the user.
Input Format: 
n = No. of elements in a list 
l = list where input elements should be taken from the user 
Output Format: 
• Print the list 
• Print only the positive numbers from the list “l”. 
Constraints: 
• For input in “l”, if “n” exceeds the declared value of n, then list will display only up to  
declared “n” values, e.g., n = 3 and input for l = [10 -12 45 -78 90], the printed l = [10  -12 45]. 
• If length of “l” < n, the code will continue with that list. 
Sample Input: 
6 
[-10, 4, -1, -40, -56, 20] 
Sample Output: 
4, 20'''

n = int(input())
number = []

for i in range(1,n+1):
    x = int(input())
    number.append(x)
print(number)

for i in number:
    if i > 0:
        print(i,end=" ")
    else:
        pass
