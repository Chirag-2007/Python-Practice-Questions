'''2. Problem Statement ) Mrs Roopam locate two coins from a box (containing a set of coins 
e.g. 1, 2, 5, 10, 20 etc.) which have a maximum sum. She is confused and is not able to find 
the required pair, help him to find the solution with the help of a python program using 
list.'''

n = int(input())
number = []

for i in range(1,n+1):
    m = int(input())
    number.append(m)

max_sum = 0
num1 = 0
num2 = 0

for i in range(0,n):
    for j in range(i+1,n):
        total = number[i] + number[j]
        if max_sum < total:
            max_sum = total
            num1 = number[i]
            num2 = number[j]

print(num1,num2)