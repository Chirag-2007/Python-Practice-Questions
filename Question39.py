# Write a program that reads a list of n integers and prints the largest number.

n = int(input())
num_list = []

for i in range(1,n+1):
    num = int(input())
    num_list.append(num)

print(max(num_list))