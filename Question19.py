# Star Pyramid

n = int(input("Enter n: "))

for i in range(1,n+1):
    print(" "*(n-i), end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()

# Number Pyramid

n = int(input("Enter n: "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j ,end=" ")
    print()
        