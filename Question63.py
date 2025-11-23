'''Q1 Problem Statement 
Input a list from the user that contains car brand names. The task is to find the length of each brand 
name and print it. Also print the concatenated output of brands with the maximum length. 
Input Format: 
Enter the number of brands: n (integer value) 
Output Format: 
Concatenated string with maximum number of characters 
Sample input 
3 
Volvo 
Bentley 
Porsche 
Sample output: 
5 
7 
7 
Bentley Porsche 
Input 1:  
3 
Polonez  
Audi  
Porsche  
Output:  
7 
4 
7 
Polonez Porsche 
Input 2:  
3 
Charmant  
Jeep  
Chrysler   
Output:  
8 
4 
8 
Charmant Chrysler 
Input 3:   
DO NOT WRITE ANYTHING ON QUESTION PAPER EXCEPT ROLL NO. 
3 
Toyota  
Tesla  
Trofeo   
Output: 
6 
5 
6 
Toyota Trofeo 
Input 4:  
2 
Tata  
Ferrari  
Output:  
4 
7 
Ferrari 
Input 5:  
2 
Mercedes  
Maverick  
Output:  
8 
8 
Mercedes Maverick 
Input 6:  
3 
Maruti  
Hyundai  
Honda  
Output:  
6 
7 
5 
Hyundai '''

n = int(input())
name_arr = []

for i in range(1,n+1):
    name = input()
    name_arr.append(name)

for i in name_arr:
    print(len(i))

max_len = 0
for i in name_arr:
    if len(i) > max_len:
        max_len = len(i)

for i in name_arr:
    if len(i) == max_len:
        print(i,end=" ")



    
