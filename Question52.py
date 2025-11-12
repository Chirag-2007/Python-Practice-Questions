'''Problem Statement 8: Incremented Salary calculator  
An organization made a policy for annual appraisals for the employees. According to the 
policy, if the gender of the employee is female then 15% of the current gross salary or if the 
gender of the employee is male then 10% of the current gross salary is added in the current 
gross salary of the employee to generate his/her new gross salary. Write a program in python 
which can accept the input as the basic salary of the employee along with his/her current 
gross salary and the gender of the employee as 'M' for male or 'F' for Female. Then the 
program will print the new Gross salary of the employee as the sum of current gross salary 
and increment (10% or 15%) based on gender. In case of wrong gender information the 
program will print " wrong input" 
Input Format 
First line of input contains the current gross salary of the employee 
Second line of input contains the gender information of employee as "M" or "F" for male and 
female respectively. 
Output Format 
Print new gross salary of the employee 
Sample Input-1 
1000 
M 
Sample Output-1 
1100.0 
Sample Input-2 
1000 
F 
Sample Output-2 
1150.0 
Sample Input-3 
1000 
K 
Sample Output-3 
wrong input '''

def male(x):
    increment = (x * 10)/100
    x = x + increment
    return x

def female(x):
    increment = (x * 15)/100
    x = x + increment
    return x

x = float(input())
alpha = input()

if alpha == "M":
    print(male(x))
elif alpha == "F":
    print(female(x))
else:
    print("wrong input")

