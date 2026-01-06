# Q11. Placeholder Loop (pass)

n = int(input())

for i in range(1,n+1):
    if i == 5:
        pass
    print(i)

# Q12. Simple Adder Function (Defining & Calling)

def add_numbers(a, b):
    return a + b

a,b = map(int,input().split())
output = add_numbers(a,b)
print(output)

# Q13. Student Info Printer (Keyword Arguments)

def print_student(name, age):
    return ("Name:", name + ",", "Age:", age)

name = input()
age = int(input())
print(print_student(name,age))

# Q14. Power Calculator (Default Argument)

def power(base,exp=2):
    return base ** exp

base = int(input())
exp = input()

if exp == "":
    print(power(base))
else:
    exp_int = int(exp)
    print(power(base,exp_int))

# Q15. Total of Variable Numbers (Variable-Length Arguments)

def add(*nums):
    sum = 0
    for i in num:
        sum = sum + i
    return sum

n = int(input())
num = list(map(int,input().split()))
print(add(*num))