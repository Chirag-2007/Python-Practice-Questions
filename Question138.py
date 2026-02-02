'''City Traffic Jam Monitor

The city's transport department monitors highway conditions minute-by-minute, logging the state as either 'F' (Free Flowing) or 'S' (Slow/Stuck).

They want to identify the maximum duration of a single, continuous traffic jam.
You must analyze the traffic log's string traffic_log and determine the longest sequence of consecutive 'S' (Slow/Stuck) entries.

Input Format:

Given a sequence of single-character traffic states in string traffic_log.

Output Format:

Find and print the integer value representing the longest sequence of consecutive 'S' (Slow/Stuck) entries.

Sample Input:
FSSSFFSSSSSF

Sample Output:
5'''

word = input()
count = 0
max_count = 0

for i in word:
    if i == "S":
        count = count + 1
        if max_count <  count:
            max_count = count
    else:
        count = 0

print(max_count)