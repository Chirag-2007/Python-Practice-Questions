# Q16. Symmetric Difference of Words (Sorted Deterministic)

word_1 = input().split()
word_2 = input().split()

set_word_1 = set(word_1)
set_word_2 = set(word_2)

not_common = set_word_1.symmetric_difference(set_word_2)
print(list(not_common))

# Q17. Append and Count in List (Deterministic)

number = list(map(int,input().split()))
n = int(input())
number.append(n)
print(number)

total = 0
for i in number:
    if i == n:
        total =  total + 1
print(total)

# Q18. Insert at Index with Bounds

num = list(map(int,input().split()))
index,value = list(map(int,input().split()))

num.insert(index,value)
print(num)

# Q19. Remove First Occurrence or Print NoChange

num = list(map(int,input().split()))
x = int(input())

if x in num:
    num.remove(x)
    print(num)
else:
    print("NoChange")

# Q20. Extend Two Lists and Print Sorted

num_1 = list(map(int,input().split()))
num_2 = list(map(int,input().split()))

num_1.extend(num_2)
print(sorted(num_1))

