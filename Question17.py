# reverse a number --> Important Code

num = int(input("Enter a number: "))
length = len(str(num))
reverse_num = 0
original_num = num

for i in range(1,length+1):
    last_num = original_num % 10
    reverse_num = last_num * (10 ** (length-i)) + reverse_num
    original_num = original_num // 10

print("The reverse number is:",reverse_num)


