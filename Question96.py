# Q1. Even Squares Using List Comprehension (Deterministic)

n = int(input())
even_square = [x**2 for x in range(1,n+1) if x % 2 == 0]
print(even_square)

# Q2: Convert Celsius to Fahrenheit

num = list(map(int,input().split()))

fahrenheit = [f"{((9/5) * x + 32):.2f}" for x in num]
print(fahrenheit)

# Q3. Keep Palindromes with filter (Case-Sensitive)

sent = list(input().split())

palindrome_sent = [x for x in sent if x == x[::-1]]
print(palindrome_sent)

# Q4. Sum of Odds (filter + reduce)

from functools import reduce

n = list(map(int,input().split()))

odd_num = [x for x in n if x % 2 != 0]

if odd_num:
    odd_sum = reduce(lambda x,y: x + y,odd_num)
else:
    odd_sum = 0
print(odd_sum)

# Q5. Count Vowels (Case-Insensitive)

word = input()
vowel = "aeiouAEIOU"

vowel_count = sum(1 for x in word if x in vowel)
print(vowel_count)