'''A school is planning to buy notebooks for students from one of two suppliers.
Each supplier has quoted a price for a single notebook:
Supplier A charges X rupees per notebook
Supplier B charges Y rupees per notebook
To reduce expenses, the school must choose the supplier offering the lower price.
Given the quoted prices X and Y, determine which supplier is more economical by reporting the lowest price among the two.
Input
Each test case contains 2 numbers a and b, separated by a space where a not equal to b.
Output
Print the smallest number.
Sample Input 1
10 
20
Sample Output 1
10'''

n = int(input())
m = int(input())

if n < m:
    print(n)
else:
    print(m)