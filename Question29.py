# Plants and height of plants

n = int(input("Enter n: "))
list1 = []
sum = 0

for i in range(1,n+1):
    num = int(input("Enter list items: "))
    list1.append(num)

for i in range(0,n):
    sum = sum + list1[i]

average = sum // n
print("The average height value on a single line:",average)

