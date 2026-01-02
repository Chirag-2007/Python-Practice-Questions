# Q51. Longest Row Index (Jagged Lists)

n = int(input())
jag_arr = []

if n == 0:
    print("-1")
else:
    for i in range(1,n+1):
        x = list(input().split())
        jag_arr.append(x)

    max_index = 0
    for i in range(0,n):
        if max_index < len(jag_arr[i]):
            max_index = i

    print(max_index)

# Q52. Count Non-Overlapping Substrings (Strings)

s = input()
sub = input()

count = 0
i = 0

while i < len(s):
    if s.startswith(sub, i):
        count += 1
        i += len(sub)
    else:
        i += 1

print(count)

# Q53. Remove Adjacent Duplicates (Strings)

word = input()

final = ""
prev = ""

for ch in word:
    if ch != prev:
        final = final + ch
        prev = ch

print(final)

# Q54. Anagram Check (Case/Space-Insensitive)

word_1 = input().lower()
word_2 = input().lower()

if sorted(word_1) == sorted(word_2):
    print("Anagram")
else:
    print("Not")

# Q55. Pangram Check (Strings)

s = input().lower()

letters = {c for c in s if 'a' <= c <= 'z'} # set ma taki sare character count kr paye amd duplicate na aaye dubara
print("Yes" if len(letters) == 26 else "No") # len(letter) == 26 this means that all teh alphabets are there in the string s