# Reverse String

str = input("Enter a string: ")

words = str.split() # split() function thod deta h string ko list ki form ma
rev_words = [word[::-1] for word in words] #word[::-1] hr element ko reverse kr deta h and (word in words) wale se list ke hr element ko reverse karega 1 by 1

result = " ".join(rev_words) # last ma (" ".join) isse join kr dega hr element ko or bich ma space ajaenge

print(result)