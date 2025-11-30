# Write a program to read 2 lines of integers and print their sorted intersection using set

set1 = {1,2,3,4,5,6,8}
set2 = {2,4,6,7,8,9}
sorted_set = set1.intersection(set2)
print (sorted(set(sorted_set)))

# From a list of integer keep the number divisble by 3 and print thier square list(filter  + comprehension)

list2 = [1,2,3,4,5,6,7,8,9]
divisible_3 = list(filter(lambda x: x % 3 == 0,list2))

square_number = [z**2 for z in divisible_3]
print(square_number)

# remove the first occurance of x from the list if not present print no change

list1 = [1,2,3,2]
x = int(input())

if x in list1:
    list1.remove(x)
    print(list1)
else:
    print(list1)