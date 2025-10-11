# Minimum of 2 numbers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("The minimum of 2 numbers is:",min(a,b))

# Minimum of 3 numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a < b and a < c:
    print(a,"is the minimum number")
elif b < a and b < c:
    print(b,"is the minimum number")
else:
    print(c,"is the minimum number")