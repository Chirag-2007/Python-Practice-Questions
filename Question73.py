'''Question 2
Question Preview
Coding
Bookstore Inventory Tracker
Testcase: 6
Description:
Read N books and their stock counts, store them in a dictionary, and print the total number of books available.nput Format:
•	First line: integer N
•	Next N lines: <book_name> <count>
Output Format:
•	{'Total Books': <sum>}
Sample Test Case:
Input
3
Python101 12
AIforKids 18
DataScience 10
Output
{'Total Books': 40}'''

n = int(input())
emp_dict = {}
total = 0

for i in range(1,n+1):
    book = input().split()
    book_name = book[0]
    count = int(book[1])
    emp_dict[book_name] = count
    total = total + count

# OR
# total = sum(emp_dict.values())

print({'Total Books':total})
    
