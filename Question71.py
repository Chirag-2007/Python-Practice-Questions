#(1) From 2 lines of words print sorted list of words thar appear in exactly one line (str,set,symmatric_difference)
# n = "red blue green"
# m = "blue yellow"

#(2) Print the size of union of 2 sets 
# 1 2 3
# 3 4
# output --> 4

# (3) Read an integers convert to tuple print the tuple and the sum if its elements

# (4) Swap the maximum and minimum value in the tuple

# (5) Build a dictionary {character:count} for a non space character using dictionary comprehension
# Input --> abab
# Output -->
# a:2
# b:2

# Question 1 -->

n = input().split()
m = input().split()

set1 = set(n)
set2 = set(m)

set3 = set1.symmetric_difference(set2)

for i in set3:
    print(i,end=" ")

# Question 2 -->

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

set1 = set(arr1)
set2 = set(arr2)

union_set = set1.union(set2)
print(len(union_set))

# Question 3 -->

list1 = [1,2,3,4,5]
list_to_tuple = tuple(list1)
print(list_to_tuple)

total = 0
for i in list_to_tuple:
    total  = total + i
print(total)

# Question 4 -->

tuple1 = tuple(map(int,input().split()))
list1 = list(tuple1)

max_num = list1.index(max(list1))
min_num = list1.index(min(list1))

for i in list1:
    temp = list1[max_num]
    list1[max_num] = list1[min_num]
    list1[min_num] = temp

list_to_tuple = tuple(list1)
print(list_to_tuple)

# Question5 -->
    
n = input()
chars = [c for c in n if c!= ' ']
freq = {c:chars.count(c) for c in set(chars)}
print(freq)