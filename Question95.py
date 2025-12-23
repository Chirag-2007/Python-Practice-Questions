# Topic 4: Strings — Introduction, Methods, Comprehension & Properties (5 Questions)

# Q1 Count Vowels and Consonants in a Sentence

sent = input().lower()
vowels = "aeiou"

vowels_count = sum(1 for x in sent if x in vowels)
consonent_count = sum(1 for x in sent if x.isalpha() and x not in vowels)

print("Vowels:",vowels_count)
print("Consonants:",consonent_count)

# Q2 Palindrome Checker (Ignoring Spaces & Case)

sent = input().lower().replace(" ","")

if sent == sent[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")