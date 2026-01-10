# Q31. Character Frequency Dictionary

s = input()
freq = {}

for ch in s:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

for ch in freq:
    print(ch, freq[ch])

# Q32. Word Length Dictionary (Dictionary Comprehension)

sent = input().split()
emp_dict = {}

for i in sent:
    name = i
    length = len(i)
    emp_dict[name] = length

for w in emp_dict:
    print(w, emp_dict[w])

# Q33. Dice Roll Simulator (Built-in Modules, Random)

import random

n = int(input())

for i in range(1,n+1):
    final = random.randint(1,6)
    print(final)

# Q34. Square Root Calculator (math Module, Attributes)

import math

n = int(input())

sq_root = math.sqrt(n)
value = math.pi

print(sq_root)
print(value)

# Q35. Write and Read Numbers from File (File I/O)

N = int(input())

with open("numbers.txt", "w") as f:
    for i in range(1, N+1):
        f.write(str(i) + "\n")

total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line)

print(total)