# Topic 1: List Comprehension -->

# Q1: Square Numbers with Conditions

n = int(input())

even_num = [x for x in range(1,n+1) if x % 2 == 0]
even_square = [n**2 for n in even_num]
print(even_square)

# Q2: Extract Vowels from Word List

n = input().split()
vowels = ['a','e','i','o','u','A','E','I','O','U']

vowel_start = [x for x in n if x[0] in vowels]
print(vowel_start)

# Q3: Generate Multiples of 3

n = int(input())
multiple_3 = [x for x in range(1,n+1) if x % 3 == 0]
print(multiple_3)

# Q4: Character Frequency Dictionary

chr_num = list(input())
length = len(chr_num)
emp_dict = {}

for i in range(0,length):
    count = 0
    for j in range(0,length):
        if chr_num[i] == chr_num[j]:
            count = count + 1
    emp_dict[chr_num[i]] = count

print(emp_dict)

# Q5: Convert Celsius to Fahrenheit

num = list(map(int,input().split()))

fahrenheit = [f"{((9/5) * x + 32):.2f}" for x in num]
print(fahrenheit)







