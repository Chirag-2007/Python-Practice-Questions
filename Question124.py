'''Write a program to enter cost price and selling price of a product and find profit or loss incurred. If cost price and selling price are same then print No Profit No Loss.
Sample Input 1
7//Cost Price
9//Selling Price
Sample Output1
Profit=2
Sample Input 2
9
9
Sample Output 2
No Profit No Loss
Sample Input 3
100
90
Sample Output 3
Loss=10'''

cp = int(input())
sp = int(input())

if cp < sp:
    profit = sp - cp
    print("Profit=" + str(profit))
elif cp > sp:
    loss = cp - sp
    print("Loss=" + str(loss))
else:    
    print("No Profit No Loss")

# IMPORTANT POINT -->
# If we use print("Profit="+profit) then one space will come in the output so the test cases will not run
# so to to solve the problem we use  print("Profit=" + str(profit)).....