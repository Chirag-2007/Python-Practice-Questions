# Anagram string -> Important Question

str1 = input("Enter 1st alphabet:")
str2 = input("Enter 2nd alphabet:")

str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2): # Sorted() -> in-built function h jo string ko list ma ascending order ma convert ke deta h
    print("Anagram")
else:
    print("Not a Anagram")