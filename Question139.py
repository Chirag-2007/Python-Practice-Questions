'''Sports Player Game Stats

A sports team manager tracks player statistics during a season.
Each record includes the Player Name, the Game Type, and the Points Scored.
Some scores were incorrectly logged as fractions or text.

You must:

Determine the Total Points Scored for each Player Name.

Only integer scores are valid.
For non-integer score, print a message "Invalid record skipped" for this.

Print the final statistics with the key and value separated by a colon, all within a dictionary structure.

Input Format:

A list of tuples
(Player Name, Game Type, Points Scored)

Output Format:

Dictionary
{Player Name : Total Points}

Sample Input 1:
[('Mayank', 'A', 10), ('Rohit', 'B', 5), ('Mayank', 'D', 15)]

Sample Output 1:
{'Mayank': 25, 'Rohit': 5}

Sample Input 2:
[('Mia', 'A', 10), ('Zoe', 'B', 5), ('Mia', 'B', 15), ('Zoe', 'A', 'five')]

Sample Output 2:
Invalid record skipped
{'Mia': 25, 'Zoe': 5}'''

n = eval(input())
emp_dict = {}

for i in n:
    name,game,point = i
    if not isinstance(point,int):
        print("Invalid record skipped")
        continue
    else:
        if name in emp_dict:
            emp_dict[name] += point
        else:
            emp_dict[name] = point

print(emp_dict)