'''Problem Statement 3) A trainee programmer develop a module in which he/she needs to print the 
first name, middle name in short with dot and the last name in full. He/She seeks the difficulty in 
developing the code in python. You have to suggest a suitable code and help a trainee programmer 
to develop the code for the same.
INPUT: 
Vishal Kumar 
OUTPUT: 
V. Kumar'''

n = input()
parts = n.split()
length = len(parts)
short_name = ""

if length == 1:
    print(parts[0])
else:
    for i in range(0,length-1):
        short_name = short_name + parts[i][0].upper() + "."

short_name = short_name + " " + parts[length-1].title()
print(short_name)
