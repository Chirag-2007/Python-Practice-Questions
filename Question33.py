'''Q2. Rahul is a beginner to write a code. He is a studious student and very curious to solve mathematics problems. His teacher gave him an assignment to check whether a given number is a prime or not. Mathematically, he solved the problem well. But, other computer faculty ask him to write a python code for this problem. Help him to check whether a given number is a prime number or not.
 *Prime numbers are those numbers which are divisible by 1 and itself only.
Sample Input 1
56
Sample Output 1
not prime
Sample Input 2
23
Sample Output 2
prime'''

n = int(input())
num = n
prime_number = True

if n <= 1:
    print("not prime")
else:
    for i in range(2,n):
        if n % i == 0:
            prime_number = False
            break

if prime_number == True:
    print("Prime")
else:
    print("Not prime")