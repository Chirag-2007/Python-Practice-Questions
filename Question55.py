'''Problem Statement 4: Print the following pattern using nested for loops 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
Input Format
The number of lines 
Constraints 
NIL 
Output Format 
The aforesaid pattern  
Sample Input 
5 
Sample Output 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* *  
*'''

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print("*",end=" ")
    print()
