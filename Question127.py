'''Package Delivery Time Audit

A courier service tracks delivery times (in minutes).

A delivery taking 40 minutes or less is classified as "On Time".
A delivery taking longer than 40 minutes is "Delayed".
The day’s log ends with a record of -1.

Your Task:

Process the list of delivery times.

Count the number of "On Time" deliveries (<= 40) and "Delayed" deliveries (> 40).
Stop counting when the end marker (-1) is reached.

Input Format:
A single list representing the delivery times.

Output Format:
Tuple (on_time_count, delayed_count)

Note: you have to return the resultant tuple.

Sample Test case 1:

Input:
[15, 32, 28, 30, 40, -1]

Output:
(5, 0)

Sample Test case 2:

Input:
[10, 20, 45, -1]

Output:
(2, 1)'''

def delivery_time_audit(times):
    on_time_count = 0
    delay_count_num = 0

    for i in times:
        if i == -1:
            break
        if i <= 40:
            on_time_count += 1
        else:
            delay_count_num += 1

    return (on_time_count, delay_count_num)

times = eval(input())
print(delivery_time_audit(times))