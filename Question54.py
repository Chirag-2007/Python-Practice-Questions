'''Problem Statement3 : Print the following inverted pyramid number pattern: 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
Input Format 
The number of lines 
Constraints 
NIL 
Output Format 
The aforesaid pattern  
Sample Input 
5 
Sample Output 
1 2 3 4 5 
1 2 3 4  
1 2 3  
1 2  
1  '''

n = int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()