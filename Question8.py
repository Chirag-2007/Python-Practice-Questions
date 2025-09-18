# Triangle pattern

# Method 1

n = int(input("Enter n: "))

for i in range(1, n+1):
    print("*"*i)

# Method 2

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()

# Number Triangle

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()