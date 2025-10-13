# GCD of 2 numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))
gcd = 1

for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("Gcd of 2 numbers is:",gcd)
