'''Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to 
compute the average of all the plants with distinct heights in her greenhouse. 
Formula used: 
Average = Sum of Distinct Heights / Total Number of Distinct Heights 
Input Format 
The first line contains the integer, N, the total number of plants. 
The second line contains the N space separated heights of the plants.  
 
DO NOT WRITE ANYTHING ON QUESTION PAPER EXCEPT ROLL NO. 
Constraints 
0 < N <= 100 
Output Format 
Output the average height value on a single line. 
Sample Input 
10 
161 182 161 154 176 170 167 171 170 174 
Sample Output 
169 '''

total_plants = int(input())
height_plant = []

for i in range(1,total_plants+1):
    height = int(input())
    height_plant.append(height)

sum = 0
set_height_plant = set(height_plant) # Typecast into set because they have asked for distinct heigths

for i in set_height_plant:
    sum = sum + i

average_height = sum / len(set_height_plant)
print(round(average_height))

