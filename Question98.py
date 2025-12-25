# Q11. Main Diagonal Sum (2-D Lists)

n = int(input())
matrix = []

for i in range(1,n+1):
    x = list(map(int,input().split()))
    matrix.append(x)

sum = 0
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            sum = sum + matrix[i][j]
print(sum)

# Q12. Squares of Numbers Divisible by 3

num = list(map(int,input().split()))

divisible_3 = list(filter(lambda x: x % 3 == 0,num))
square_num = [x**2 for x in divisible_3]
print(square_num)

# Q13. Title Case Except Stopwords (stopwords {a, an, the, of, and, in})

sent = input().split()
stopwords = ['a','an','the','of','and','in']
updated = []

for i in range(0,len(sent)):
    if i == 0:
        updated.append(sent[0].title())
    else:
        if sent[i] in stopwords:
            updated.append(sent[i])
        else:
            update_word = sent[i].title()
            updated.append(update_word)
print(" ".join(updated))

# Q14. Reverse Substring by Indices (Bounds Checked)

word = input()
length = len(word)
index_1, index_2 = map(int, input().split())

if 0 <= index_1 <= index_2 < length:
    reverse = word[index_1:index_2+1][::-1]
    print(word[:index_1] + reverse + word[index_2+1:])
else:
    print("Invalid")

# Q15. Squares of Odd Numbers as Dict Pairs (Deterministic)

num = list(map(int,input().split()))
emp_dict = {}

for i in num:
    if i % 2 != 0:
        number = i
        sqaure_num = i**2
        emp_dict[number] = sqaure_num
output = sorted(emp_dict.items())
print(output)
    