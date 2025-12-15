'''Question 7
Question Preview
Coding
Sports Tournament Scorer
Description:
Store the scores of N players in 3 matches each.
Then calculate and print the total score for each player as {name: total}.
Input Format:
•	First line: integer N
•	Next N lines: <player_name> <score1> <score2> <score3>
Output Format:
•	Dictionary {player_name: total_score}
Sample Test Case:
Input
3
Riya 10 20 30
Karan 15 25 20
Meena 30 35 25
Output
{'Riya': 60, 'Karan': 60, 'Meena': 90}'''

n = int(input())
emp_dict = {}
for i in range(1,n+1):
    data = input().split()
    name = data[0]
    number = data[1:]
    total = 0
    for i in number:
        total = total + int(i)
    emp_dict[name] = total
print(emp_dict)
    