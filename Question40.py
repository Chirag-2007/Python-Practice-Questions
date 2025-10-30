'''CODING
First K Primes (Break/Continue)

Given integer k (1-50), print the first k prime numbers on one line separated by a single space. Use loops; stop generating as soon as you have k primes. If k is invalid, print INVALID.

Input
One integer k.

Output
Either INVALID or a single line with k primes separated by spaces.'''

k = int(input())

if k < 1 or k > 50:
    print("INVALID")
else:
    count = 0
    num = 2
    while count < k:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
            count += 1
        num += 1



