# Q36. Tuple Max and Min (Tuples)

num = tuple(map(int,input().split()))

if len(num) == 0:
    print("None None")
else:
    max_num = max(num)
    min_num = min(num)
    print(max_num,min_num)

# Q37. Concatenate Two Tuples (Tuples)

num_1 = tuple(map(int,input().split()))
num_2 = tuple(map(int,input().split()))

num_1_list = list(num_1)
num_2_list = list(num_2)

num_1_list.extend(num_2_list)

print(tuple(num_1_list))

# Q38. Remove Duplicates from Tuple (Deterministic Sorted)

num = tuple(map(int,input().split()))

set_num = set(num)
output = sorted(set_num)
print(tuple(output))

# Q39. Merge Two Dictionaries by Summing Values (Deterministic Pairs)

d1 = eval(input())
d2 = eval(input())

merged = {}

for k in d1:
    merged[k] = merged.get(k, 0) + d1[k]
for k in d2:
    merged[k] = merged.get(k, 0) + d2[k]

result = sorted(merged.items())
print(result)

# Q40. Character Type Counts (Deterministic Dict Pairs)

n = input()

result = {
    "digits": sum(x.isdigit() for x in n),
    "alphabets": sum(x.isalpha() for x in n),
    "spaces": n.count(" "),
    "others": sum(not x.isalnum() and x != " " for x in n)
}
final = list(result.items())
print(final)




