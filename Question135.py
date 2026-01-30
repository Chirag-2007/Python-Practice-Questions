'''Q4.  National Robotics League Robot Performance Summary
During the National Robotics League, each robot competes in multiple technical challenge rounds.
Each challenge assigns a performance score based on speed, accuracy, and task completion
efficiency.The competition committee stores these scores in a dictionary where the key is the robot’s
name and the value is a list containing its scores from various challenge stages.The committee now
requires a structured report summarizing the performance of each robot.
Instruction/Task
Analyze the given robot performance data and generate a final evaluation summary.
For each robot:
1. Find Total Performance Score- Add all challenge scores.
2. Compute Average Mission Score → total_score / mission_count, rounded to 2 decimals.
3. Assign Robotics Grade
Use the following grading bracket:
A → Average ≥ 75
B → 50 ≤ Average < 75
C → Average < 50
4.Construct Output Dictionary: The result must map each robot to:
(total_score, average_score, grade)
Return this final summary dictionary.
Note:
While calculating the average mission score, use the round() function to round the value to 2 decimal
places.
Example:
average_score = round(total_score / mission_count, 2)
Input Format:
{RobotName : [score1, score2, score3, ...]}
Output Format:
{RobotName : (total_score, average_score, grade)}
Sample Input 1
{'BoltX':[90,75,82], 'IronBot':[45,55,50], 'NanoR':[60,62,58]}
Sample Output 1
{'BoltX': (247, 82.33, 'A'), 'IronBot': (150, 50.0, 'B'), 'NanoR': (180, 60.0, 'B')}
Sample Input 2
{'Alpha':[78,85,80], 'Beta':[35,40,45]}
Sample Output 2
{'Alpha': (243, 81.0, 'A'), 'Beta': (120, 40.0, 'C')}

OR

Q5.  Online Gaming Arena Player Rank Generator
An online gaming platform tracks players’ performance across multiple gaming missions.
Each mission gives a score, and these mission scores are stored in a dictionary with player names as
keys.
The gaming system requires a performance ranking summary to assign reward tiers.
Instruction/Task
For each player:
1. Compute Total Mission Score → sum of all mission scores.
2. Compute Average Mission Score → total_score / mission_count, rounded to 2 decimals.
3.Assign Reward Rank:
Rank 'A' → Average ≥ 75
Rank 'B' → 50 ≤ Average < 75
Rank 'C' → Average < 50
4.Prepare a new dictionary where each player maps to:
(total_mission_score, average_score, reward_rank)
Return this final reward summary.
Note:
While calculating the average score, use the round() function to round the value to 2 decimal places.
Example:
average_score = round(total_score / number_of_rounds, 2)
Input Format:
Dictionary mapping:
{PlayerName : [mission_score1, mission_score2, ...]}
Output Format:
Dictionary mapping:
{PlayerName : (total, average, rank)}
Sample Input 1
{'Max':[70,80,75], 'Lina':[40,50,45]}
Sample Output 1
{'Max': (225, 75.0, 'A'), 'Lina': (135, 45.0, 'C')}
Sample Input 2
{'Rex':[85,90,88], 'Mini':[55,52,58]}
Sample Output 2
{'Rex': (263, 87.67, 'A'), 'Mini': (165, 55.0, 'B')}

OR

Q6.  Corporate Fitness Challenge Employee Score Evaluator
A company arranged a “Fitness Challenge Week,” where employees participated in multiple fitness
rounds. Each employee’s performance score in every round is stored in a dictionary. The management
wants a structured analysis of overall fitness levels based on their cumulative performance.
Instruction/Task
Process the given employee fitness score record.
For each employee:
1. Compute Total Score → summation of all round scores.
2. Compute Average Score → total_score / number_of_rounds (rounded to 2 decimals).
3. Determine Fitness Category:
‘A’ → Avg ≥ 75
‘B’ → 50 ≤ Avg < 75
‘C’ → Avg < 50
4.Construct a results dictionary mapping each employee to:
(total_score, average_score, fitness_grade)
Return the final evaluation report.
Note:
While calculating the average score, use the round() function to round the value to 2 decimal places.
Example:
average_score = round(total_score / number_of_rounds, 2)
Input Format:
Dictionary mapping:
{EmployeeName : [score1, score2, ...]}
Output Format:
Dictionary mapping:
{EmployeeName : (total, average, grade)}
Sample Input 1
{'Rohit':[60,75,80], 'Sameer':[40,45,50]}
Sample Output 1
{'Rohit': (215, 71.67, 'B'), 'Sameer': (135, 45.0, 'C')}
Sample Input 2
{'Divya':[90,85,95], 'Kritika':[55,60,50]}
Sample Output 2
{'Divya': (270, 90.0, 'A'), 'Kritika': (165, 55.0, 'B')}'''

def national_robotics(name_num):
    emp_dict = {}
    for name in name_num:
        num = name_num[name]
        total = 0
        for i in num:
            total = total + i
        avg = round(total / len(num), 2)

        if avg >= 75:
            grade = "A"
        elif avg >= 50:
            grade = "B"
        else:
            grade = "C"
        emp_dict[name] = (total, avg, grade)
    return emp_dict

x = eval(input())
print(national_robotics(x))