'''Q1. Reena and Teena are twin sisters. They got admission in BTech. Computer science and Engineering in Chitkara University. Their teacher taught then about the coding concepts and gave them an assignment to write a program to find the greatest among three numbers. Help both sisters to find the greatest among three numbers.
Sample input 1
34
67
78
Sample Output 1
78
Sample input 2
335
167
178
Sample Output 2
335
Explanation:
Sample Input: Input 3 numbers from user
Sample Output: Display the greatest among three numbers'''

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)