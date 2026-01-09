# Q26. Count Vowels in a String (String Methods)

word = input()
vowels = "aeiouAEIOU"
count = 0

for i in word:
    if i in vowels:
        count = count + 1
print(count)

# Q27. Remove Spaces Using String Comprehension

sent = input()
no_space = [x for x in sent if x!=" "]
final = "".join(no_space)
print(final)

# Q28. Clean Palindrome Checker (Ignoring Case and Spaces)

sent = input().lower().strip()
no_space = [x for x in sent if x!=" "]

if no_space == no_space[::-1]:
    print("Yes")
else:
    print("No")

# Q29. Tuple Statistics (Max, Min, Average)

n = int(input())
num = tuple(map(int,input().split()))
sum = 0

max_val = max(num)
min_val = min(num)

for i in num:
    sum = sum + i
avg = sum // n

print(max_val)
print(min_val)
print(avg)

# Q30. Unique Words Using Set

sent = input().split()
set_num = set(sent)
print(len(set_num))