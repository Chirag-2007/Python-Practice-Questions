# Hollow Inverted Triangle

n = int(input("Enter n: "))

for i in range(n,0,-1):
    for j in range(i,0,-1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Hollow Triangle

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if i == 1 or i == n or j == 1 or j == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

