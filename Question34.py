'''QUESTION 3
Rohan and Ajay are playing a game. The game says, they have been given a list of numbers and they have to find out a pair in the list having maximum sum. Ajay is confused and is not able to find the required pair, help him to find the solution.
You have given a list A containing N elements. Your task is to find the pair of numbers in the list having maximum sum.
Write a python program which takes the size N and the list A as input and print the maximum sum pair separated by space as the output.
INPUT FORMAT:
The first line contains an integer N denoting the total number of elements in the list
The next N line contains N integers representing the elements in of the list
OUTPUT FORMAT:
Print in a single line, the pair of elements from the list having the maximum sum'''

n = int(input())
num = []

for i in range(1,n+1):
    number = int(input())
    num.append(number)

for i in range(0,n):
    for j in range(i+1,n):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

sum = num[n-1] + num[n-2]
print(num[n-1],",",num[n-2],"are the pairs and the max sum is:",sum)