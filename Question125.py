'''Convert temperatures from Celsius to Fahrenheit.

Rajan is working on a weather application that requires the ability to convert temperatures from Celsius to Fahrenheit. As part of this task, he needs to implement a function that takes a temperature in Celsius as input and converts it to Fahrenheit using the formula:

Fahrenheit = (Celsius * 9/5) + 32

This feature is essential for displaying temperatures in a user-friendly format within the application.

Input Format:
The only line of input contains a single integer representing the temperature in Celsius.

Output Format:
The only line of output should print the temperature converted to Fahrenheit, rounded to two decimal places.

Code Constraints:
The input will be a single integer (which could be positive, negative, or zero).
The output should be formatted to two decimal places.

Example

Input
100

Output
212.00'''

cel = int(input())
fah = ((cel * 9/5) + 32)
print(f"{fah:.2f}")
