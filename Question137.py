'''Balloon Line Safety Check

A row of balloons is tied in a straight line.

Each balloon has a gas level inside it.

The safety checker looks at every 3 balloons next to each other.

If the total gas level of those 3 balloons is more than 60, the middle balloon bursts and disappears.

This checking keeps happening until no group of 3 balloons has gas above 60.

Your task is to return the final list of balloon gas levels after everything becomes safe.

Rules:

Look at 3 balloons next to each other.

If the total is more than 60, remove the middle one.

Sample Test Case 1

Input:
[25, 20, 30]

Output:
[25, 30]

Sample Test Case 2

Input:
[10, 45, 20, 15]

Output:
[10, 20, 15]'''

def check_balloons(balloons):
    i = 0
    while i < len(balloons) - 2:
        if balloons[i] + balloons[i+1] + balloons[i+2] > 60:
            balloons.pop(i+1)
            i = 0
        else:
            i += 1
    return balloons

n = eval(input())
print(check_balloons(n))