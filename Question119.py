'''Python Coding

Riya is playing with two numbers.

She wants to do the following:

If the product of the two numbers is even, print the sum of the numbers.

If the product of the two numbers is odd, print the difference (first number − second number).

Sample Input 1
4
5

Sample Output 1
9

Explanation:
4 × 5 = 20 (even), so we print 4 + 5 = 9.

Sample Input 2
7
3

Sample Output 2
4

Explanation:
7 × 3 = 21 (odd), so we print 7 − 3 = 4.
'''

n = int(input())
m = int(input())
product = n * m

if product % 2 == 0:
    print(n+m)
else:
    print(n-m)
    