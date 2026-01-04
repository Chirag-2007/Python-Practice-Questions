# Q1. Pass/Fail Result Checker (If–Else)

m1,m2,m3 = map(int,input().split())

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Pass")
else:
    print("Fail")

# Q2. Discount Calculator (If–Elif–Else)

amount = float(input())

if amount >= 5000:
    discount = (amount * 20)/100
    total = amount - discount
elif amount >= 2000 and amount < 5000:
    discount = (amount * 10)/100
    total = amount - discount
else:
    discount = 0
    total = amount - discount

print(total)

# Q3. Day Type Using match Statement

n = int(input())

match n:
    case 6 | 7:
        print("Weekends")
    case 1 | 2 | 3 | 4| 5:
        print("Weekdays")
    case _:
        print("Invalid")

# Q4. Even Numbers Printer (while Loop)

n = int(input())

i = 2
while i <= n:
    if i % 2 == 0:
        print(i)
    i = i + 1

# Q5. Sum of First N Natural Numbers (for Loop)

n = int(input())
total = 0

for i in range(1,n+1):
    total = total + i
print(total)