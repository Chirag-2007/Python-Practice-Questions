'''Python Coding

In the kingdom of Numberland, two warriors — each represented by a number — enter the Arena of Comparison. 
The one with the greater strength (value) becomes the Champion.

As the royal programmer, your task is to write a Python program that helps the king determine which warrior is stronger. 
You will be given two integers on a single line (space-separated), representing the strength of the two warriors. 
Your program should output the larger number.

If both warriors have equal strength, they are considered equals, and you can print either of the values (since they’re the same).

No extra messages or text should be printed — only the number representing the stronger warrior.

Input Format:
Two integers in different lines.

Output Format:
A single integer — the larger of the two numbers.

Sample Input
42
77

Sample Output
77
'''

n = int(input())
m = int(input())

if n > m:
    print(n)
else:
    print(m)