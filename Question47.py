'''1. Problem Statement 
Task: Rakesh and Rajkumar have different types of fruits in some quantities.They have 
been asked to donate all those fruits that are not in common quantities to the 
orphanage.The officials of orphanage arranged all these such categories of fruits in the 
sorted order and also displayed the count of total amount of fruits received from them. '''

n = int(input())
m = int(input())

arr_one = []
arr_two = []

for i in range(n):
    x = int(input())
    arr_one.append(x)

for j in range(m):
    z = int(input())
    arr_two.append(z)

uncommon = sorted(set(arr_one).symmetric_difference(set(arr_two)))
sum = 0

for i in uncommon:
    print(i,end=" ")
    sum = sum + i
print(sum)