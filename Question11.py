# Sum and Average in a list

list = [1,2,3,4,5]
length = len(list)
sum = 0

for i in range(0,5):
    sum = sum + list[i]
    average = sum / length

print("Sum of 5 numbers in a list is:",sum)
print("Average of 5 numbers in a list is:",average)