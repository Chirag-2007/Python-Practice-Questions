'''Fitness Challenge Reps Log

An athlete tracks their performance in a short fitness challenge, recording the time (in seconds) taken to complete a set of repetitions. A time of 60 seconds or less is deemed "Goal Met". A time greater than 60 seconds is "Needs Improvement".
The athlete signals the end of their workout data with -1.

Your Task:

Calculate the number of "Goal Met" sets (≤ 60 seconds) and "Needs Improvement" sets (> 60 seconds) from the list of times.
Stop processing when -1 is encountered.

Input Format:

A single list representing the completion times.

Output Format:

A tuple in the format:
(needs_improvement_count, goal_met_count)

Note:

You must return the resultant tuple.

Sample Test Case 1:

Input:

[15, 32, 28, 30, 40, -1]

Output:

(0,5)'''

def fitness_challenge_report(times):
    needs_improvement = 0
    goal_met = 0

    for i in times:
        if i == -1:
            break
        if i <= 60:
            goal_met += 1
        else:
            needs_improvement += 1

    return (needs_improvement, goal_met)

n = eval(input())
print(fitness_challenge_report(n))