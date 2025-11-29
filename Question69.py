# List Comprehension -->

square = [i*i for i in range(1,6)]
print(square)

# Number of Vowels in the word -->

s = input()
v = set("aeiou")
print(sum(1 for ch in s.lower() if ch in v))    

# IMPORTANT --> tuple_arr = (10,) # to declare a single element in a tuple

# create an empty tuple and remove the element from index value 3

n = int(input())

tupple_empty = ()
tuple_to_list = list(tupple_empty)

for i in range(0,n):
    x = int(input())
    tuple_to_list.append(x)

tuple_to_list.pop(3) # index 3 remove ho jaega isme

list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)