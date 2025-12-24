# Q6. Character Frequency (Deterministic Pairs)

word = input().replace(" ","")
emp_dict = {}

for i in word:
    count = 0
    for j in word:
        if i == j:
            count = count + 1
        emp_dict[i] = count

result = sorted(emp_dict.items())
print(result)

# Q7. Unique Characters Preserving First Occurrence (Stable)

word = input()

each_word = [x for x in word]
length = len(each_word)
unique_word = []

for i in range(0,length):
    if each_word[i] not in unique_word:
        unique_word.append(each_word[i])
print("".join(unique_word))

# Q8. Swap First Min and First Max in Tuple

num = tuple(map(int,input().split()))

num_list = list(num)
min_index = num_list.index(min(num_list))
max_index = num_list.index(max(num_list))

for i in num_list:
    temp = num_list[min_index]
    num_list[min_index] = num_list[max_index]
    num_list[max_index] = temp

print(tuple(num_list))

# Q9. Sorted Unique Words (Deterministic)

word = input().lower().split()

set_word = set(word)
output = list(set_word)
print(sorted(output))

# Q10. Set Intersection (Deterministic Sorted List)

num_1 = list(map(int,input().split()))
num_2 = list(map(int,input().split()))

set_num_1 = set(num_1)
set_num_2 = set(num_2)

common = set_num_1.intersection(set_num_2)
print(list(common))
            

