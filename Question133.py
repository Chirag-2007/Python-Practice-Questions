'''Water Conservation Meter

A smart meter tracks household water usage (in gallons) during short intervals.

Usage of 30 gallons or less is classified as "Low Consumption".
Usage exceeding 30 gallons is "High Consumption".
The meter stops transmitting data with a -1 signal.

Task:

Process the input list of usage.

Count the total occurrences of Low Consumption (≤ 30)

Count the total occurrences of High Consumption (> 30)

Stop processing when the list reaches the end value -1

Input Format:

List of integers representing water usage (ends with -1)

Output Format:

Tuple (low_count, high_count)

Note:

You have to return the resultant tuple

Sample Test Case 1

Input:

[10, 30, 35, 20, 45, -1]

Output:

(3, 2)'''

def water_conservation_report(usages):
    low_count = 0
    high_count = 0

    for i in usages:
        if i == -1:
            break
        if i <= 30:
            low_count += 1
        else:
            high_count += 1

    return (low_count, high_count)

n = eval(input())
print(water_conservation_report(n))