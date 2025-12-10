'''Question 7 — String Methods (Basic Usage)
Problem Statement
A user enters an email address.
Write a program to:
1.	Print the username (the part before ‘@’)
2.	Print the domain (the part after ‘@’) in uppercase.
Input Format
Single line string (email address)
Output Format
Two lines — username and domain in uppercase.
Sample Test Case 1
Input:
riya123@gmail.com
Output:
riya123
GMAIL.COM
Sample Test Case 2
Input:
arjun_k@outlook.in
Output:
arjun_k
OUTLOOK.IN
'''

email = input()

if "@" in email:
    n = email.index("@")
username = email[:n]
domain = email[n+1:].upper()

print(username)
print(domain)
