# Armstrong number -> Important Question

n = int(input("Enter a number: "))
length = len(str(n))
num = n
armstrong_num = 0

for i in range(1, length+1):
    last_num = n % 10
    armstrong_num = armstrong_num + last_num ** (length)
    n = n // 10

if armstrong_num == num:
    print("Armstrong number")
else:
    print("Not a Armstrong number")