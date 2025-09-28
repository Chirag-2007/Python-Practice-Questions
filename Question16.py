# Prime number

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime number")
else:
    prime_number = True
    for i in range(2, num):
        if num % i == 0:
            prime_number = False
            break
    
if prime_number == True:
    print("Prime Number")
else:
    print("Not a Prime Number")