# Q56. Distinct Vowels Present (Sorted List)

word = input().lower()
vowels = "aeiou"
vowels_word = []

for i in word:
    if i in vowels:
        vowels_word.append(i)

print(sorted(vowels_word))

# Q57. Product of Positive Integers (filter + reduce)

num = list(map(int,input().split()))
positive = []

for i in num:
    if i > 0:
        positive.append(i)

product = 1
for i in positive:
    product = product*i
print(product)

# Q58. Squares via map, Keep Odd Squares (LC Filter)

num = list(map(int,input().split()))
odd_num = [x for x in num if x % 2 != 0]

sqaure_num = list(map(lambda x:x*x,odd_num))
print(sqaure_num)

# Q59. Dictionary from Two Lines (Zip; Fixed Order Pairs)

alpha = list(input().split())
num = list(map(int,input().split()))

print(list(zip(alpha,num)))

# Q60. Tuple Frequency Map (Deterministic Sorted Pairs)

num = list(map(int,input().split()))
set_num = set(num)
list_num = list(sorted(set_num))
count_num = []

for i in list_num:
    count = 0
    for x in num:
        if i == x:
            count = count + 1
    count_num.append(count)

print(list(zip(list_num,count_num)))
