# Q6. Positive, Negative or Zero (Nested If)

num = int(input())

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Q7. Star Rectangle Pattern (Nested Loops)

n = int(input())
m = int(input())

for i in range(1,n+1):
    for j in range(1,m+1):
        print("*",end=" ")
    print()

# Q8. Right Triangle Pattern (range and Nested for)

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Q9. Skip Multiples of 3 (continue)

n = int(input())

for i in range(1,n+1):
    if i % 3 == 0:
        continue
    else:
        print(i)

# Q10. Stop at Negative (break)

n = int(input())
num = list(map(int,input().split()))

for i in num:
    if i < 0:
        break
    else:
        print(i)        