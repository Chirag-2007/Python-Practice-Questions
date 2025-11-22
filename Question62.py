'''Problem Statement 
Task: Ramesh and Rajkumar have M and N sets of Indian currency notes respectively. They have decided to 
donate all those currency notes that are not common to M and N to the social welfare society.  After 
receiving them, the society arranged these currency notes in sorted order and  also display the total amount 
they received     
Input Format 
The first line contains N space-separated integers.  
The second line contains M space-separated integers. 
Output Format 
The non-common elements are printed in an ascending order separated by one space and also print the 
amount of all currency notes as last elements in the same line as received by the social   welfare society   
Sample Input 
1 2 5 10             
# set of M currency notes 
5 10 100 200     # set of N unique currency notes 
Sample Output 
1 2 100 200 303      # set of noncommon currency notes  and the last element (303) is the                         
#sum of all (1+2+100+200=303) received by social welfare '''

M = list(map(int, input().split()))  # 1 line me input lene ke liye yaad rakhna h...
N = list(map(int, input().split()))

not_common = []
for i in M:
    if i not in N:
        not_common.append(i)

for j in N:
    if j not in M:
        not_common.append(j)

sorted_arr = sorted(not_common)

total = 0
for i in sorted_arr:
    total = total + i

sorted_arr.append(total)

for i in sorted_arr:
    print(i, end=" ")


