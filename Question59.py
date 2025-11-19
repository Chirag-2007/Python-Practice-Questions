'''Q 2. "MathWiz" Academy is teaching its students about the concept of recursion. To practice this 
concept, they have assigned a problem related to calculating the factorial of a given positive integer 
using recursion. 
Write a Python program that accomplishes the following: 
Define a recursive function named calculate_factorial that takes an integer n as an argument. 
Inside the function: 
Base case: If n is 0 or 1, return 1. 
Recursive case: Return n multiplied by the result of calling calculate_factorial with n-1. 
Input a positive integer num from the user. 
Call the calculate_factorial function with num as an argument and display the result. 
Your program should compute the factorial of a number using recursion. 
Sample Input 1: 
4                                                             
Sample Output 1: 
24                                                            
Sample Input 2: 
6                                                             
Sample Output 2: 
720                                                            
//integer value 
//factorial of the given number 
//integer value 
//factorial of the given number'''

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

n = int(input())
print(calculate_factorial(n))