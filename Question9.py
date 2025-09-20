# Factorial

# Method 1
n = int(input("Enter n: "))
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i

print(factorial)

# Method 2
def factorial1_to_n(n):
    if n == 0:
        return 1
    ans = n * factorial1_to_n(n-1)
    return ans

n = int(input("Enter n: "))
print("The factorial of",n,"is:",factorial1_to_n(n))

