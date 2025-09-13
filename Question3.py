# Greatest of 3 number

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

if n1 > n2 and n2 > n3:
    print(n1,"is the greatest")
elif n2 > n3 and n2 > n1:
    print(n2,"is the greatest")
else:
    print(n3,"is the greatest")

# Maximum of 2 numbers

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

print("Maximum of 2 numbers are:",max(n1,n2))