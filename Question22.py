# Palindrome number

n = int(input("Enter a number:"))
length = len(str(n))
num = n
rev_num = 0

for i in range(1, length+1):
    last_num = n % 10
    rev_num = rev_num + last_num * (10 ** (length - i))
    n = n // 10

if num == rev_num:
    print("Palindrome number")
else:
    print("Not a Palindrome number")