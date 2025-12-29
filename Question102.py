# Q31. Flatten Jagged and Return Sorted Unique (Jagged + Set)

n = int(input())
jag_list = []
num = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    jag_list.append(x)

for i in range(0,n):
    length = len(jag_list[i])
    for j in range(0,length):
        num.append(jag_list[i][j])
set_num = set(num)

print(sorted(list(set_num)))

# Q32. Longest Row Index (Jagged Lists)

n = int(input())
num_arr = []

for i in range(1,n+1):
    x = list(input().split())
    num_arr.append(x)

max_length = 0
index = 0
if n == 0:
    print("-1")
else:
    for i in range(0,n):
        if len(num_arr[i]) > max_length:
            max_length = len(num_arr[i])
            index = i

    print(index)

# Q33. Count Letters and Digits (Strings)

sent = input()

letter = sum(x.isalpha() for x in sent)
number = sum(x.isdigit() for x in sent)

print(letter,number)

# Q34. Replace Vowels with ‘*’ (String Methods)

sent = input()
vowels = "aeiouAEIOU"

for i in vowels:
    sent = sent.replace(i,"*")

print(sent)

# Q35. Words Starting with Capital (Strings)

sent = input().split()
count = 0

for i in sent:
    if i.istitle():
        count = count + 1

print(count)