# 1) List Comprehension -- >

number = [1,2,3,4,5,6,7,8,9,10]

list3 = [x for x in number if x % 2 == 0]
print(list3)

# 2) IMPORTANT QUESTION --> Convert celcius to fahrenheit using map function round upto 2 decimal places.

#Formula --> F = 9/5*(C) + 32

celsius = [24, 54, 32, 23, 87, 76]
fahrenheit = list(map(lambda x: f"{((9/5) * x + 32):.2f}", celsius))
print(fahrenheit)

# 3) Use filter function to filter the palindrome number from a list.

n = int(input())
number = []

for i in range(1,n+1):
    x = int(input())
    number.append(x)

palindrome_num = list(filter(lambda x: str(x) == str(x)[::-1],number))
print(palindrome_num)