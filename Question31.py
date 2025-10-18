# Same Alphabet in line Triangle Pattern Printing

n = int(input("Enter n: "))
num = 65

for i in range(1,n+1):
    for j in range(1,i+1):
        char = chr(num)
        print(char,end=" ")
    num = num + 1
    print()

# Flowing Alpahbet Triangle

n = int(input("Enter n: "))
num = 65

for i in range(1,n+1):
    for j in range(1,i+1):
        char = chr(num)
        print(char,end=" ")
        num = num + 1
    print()
