# Write a recursive function that takes a number n and returns the sum of its digits.

def sum(n):
    if n == 0: # Base Case
        return 0
    else:
        return (n % 10) + sum(n // 10)
    
n = int(input())
print(sum(n))