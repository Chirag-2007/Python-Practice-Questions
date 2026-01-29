'''Q1.  Cookie Jar Safety
A row of cookie jars is kept on a kitchen shelf.
Each jar has a weight.
To stop the shelf from falling, the cook checks every 3 jars next to each other.
If the total weight of those 3 jars is more than 60, the middle jar is taken away.
This keeps happening until no group of 3 jars is too heavy.
Your job is to return the final list of jar weights.
Rules :
Look at every group of 3 jars.
If their total weight is more than 60, remove the middle jar.
Keep repeating until the list is safe.
Finally, return the safe list of jar weights.
Input Format:
A list of integers showing the weight of each cookie jar.
Output Format:
A list of integers showing the safe jar weights.
Sample Test Case 1:
Input:
[20, 30, 15]
Output:
[20, 15]
Sample Test Case 2:
Input:
[10, 40, 25, 20]
Output:
[10, 25, 20]

OR

Q2.  Apple Basket Safety
A row of apple baskets is kept on a table.
Each basket has a weight.
To stop the table from breaking, the helper checks every 3 baskets that are next to each other.
If the total weight of those 3 baskets is more than 60 kg, the middle basket is removed.
This checking continues until no group of 3 baskets has a total weight above 60.
Your task is to return the final list of basket weights after everything becomes safe.
Rules :
Look at 3 baskets that are next to each other.
If the total is more than 60 kg, remove the middle basket.
Start checking again from the beginning.
Stop when no group of 3 baskets has a total over 60.
Return the final list of basket weights.
Input Format:
A list of integers showing the weight of each apple basket.
Output Format:
A list of integers showing the final safe basket arrangement.
Sample Test Case 1:
Input:
[25, 20, 30]
Output:
[25, 30]
Sample Test Case 2:
Input:
[10, 40, 25, 20]
Output:
[10, 25, 20]

OR

Q3.  Ice Cream Box Safety
A row of ice-cream boxes is kept on a freezer shelf.
Each box has a weight.
To prevent the shelf from breaking, the helper checks every 3 boxes that are next to each other.
If the total weight of those 3 boxes is more than 60 kg, the middle box is taken off the shelf.
This checking continues until no group of 3 boxes is above the limit.
Your task is to return the final safe list of box weights.
Rules :
Look at 3 boxes next to each other.
If the total is more than 60, remove the middle box.
Keep repeating until the list is safe.
Finally, return the safe list of box weights.
Input Format:
A list of integers showing the weight of each ice-cream box.
Output Format:
A list of integers showing the safe box weights after checking.
Sample Test Case 1:
Input:
[15, 40, 10, 20]
Output:
[15, 10, 20]
Sample Test Case 2:
Input:
[10, 40, 25, 20]
Output:
[10, 25, 20]'''

# Question 1 --> Rest all are same with same approach

def total_weight_jar(jars):
    length = len(jars)
    i = 0
    while i <= len(jars) - 3:
        x,y,z = jars[i],jars[i+1],jars[i+2]
        if (x+y+z) > 60:
            jars.pop(i + 1)
            i = max(i - 1, 0) # i ko 1 kam karo, lekin agar wo 0 se neeche ja raha ho to 0 hi rakho.
        else:
            i = i + 1

    return jars

jars = list(map(int,input().split()))
print(total_weight_jar(jars))