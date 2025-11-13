'''9.Average and Highest Marks 
A faculty wants to consider "N" different marks of a student and then calculate the average 
marks accordingly. Along with that out of "N" marks, the faculty needs to display the highest 
marks obtained by student in any of the subject. To handle this task , write a Python program 
to ask user the inputs like, for how many subjects, user need to enter the marks. Then user 
have to enter marks for each of the "N" subjects. The output of the program will print the 
average marks of the student in first line of output and the second line of output contains the 
highest marks entered for any of the "N" subjects entered by the user. 

Input Format 
First line of input contains the information about for how many subjects (N) faculty needs to 
enter the marks. 
Next "N" lines of inputs contains the marks entry for each subject. 
Output Format 
First line of output will print the average marks of students according to the "N" different 
marks entered by the user for each subject. 
Second line of output will print the highest marks obtained by the student in any of the "N" 
subject marks entries.  
Sample Input-1 
8   
22 
33 
44 
11 
55 
66 
77 
88 
 
Sample Output-1 
49.5 
88 
 
Sample Input-2 
3  #Total number of subjects 
50  #Marks of first subject 
60  #marks of second subject 
40  #marks of Third Subject 
Sample Output-2 
50.0  # Average marks for all subjects 
60  # highest marks by student in any of the subject'''

n = int(input())
number = []

for i in range(1,n+1):
    x = int(input())
    number.append(x)

sorted_number = sorted(number)
highest_marks = sorted_number[n-1]

sum = 0
for i in sorted_number:
    sum = sum + i
average = sum / n

print(average)
print(highest_marks)