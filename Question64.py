'''Q 2. Problem Statement
Suppose, you are given a jagged array where each row contains varying numbers of integers. Your task is to calculate the row sums of the jagged array and return the maximum row sum.
Input Format:
The first line contains an integer n (no. of rows in the jagged array). For e.g. 3.
The next n lines contain the jagged array, where each line has space-separated integers. 
For e.g;
     1 2
     3 4 5
     6 7
Output Format:
Print an integer value (maximum row sum). For e.g; 13
Code Constraints:
•	1≤ n ≤100 (The number of rows)
•	The number of elements in each row will be at least 1 and at most n.'''

n = int(input())
number_list = []

for i in range(n):
    row = list(map(int, input().split()))
    number_list.append(row)
    
sum_arr = []
length = len(number_list)

for i in range(0,length):
    sum = 0
    for j in range(0,len(number_list[i])):
        sum = sum + number_list[i][j]
    sum_arr.append(sum)

max_value = 0
for i in sum_arr:
    if max_value < i:
        max_value = i
print(max_value)

# Question2 --> Matrix List

number_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

sum_arr = []
length = len(number_list)

for i in range(0,length):
    sum = 0
    for j in range(0,len(number_list[i])):
        sum = sum + number_list[i][j]
    sum_arr.append(sum)

max_value = 0
for i in sum_arr:
    if max_value < i:
        max_value = i
print(max_value)
