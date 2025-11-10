'''4.Problem Statement1 :ShoppingCart 
Tina went to the market to buy some groceries. She filled her basket with different items. At 
the billing counter she saw a long waiting queue. She decided to make a system which helps 
the vendors automate this process. Help her to do so.  
For this you need to write a python program to create a class representing a shopping cart and 
include methods the following methods: 
1. Add items to the cart
2. Calculate the discount  
3. Calculate the total bill (after applying the discounts)
SAMPLE INPUT: 
2           
Apple 100      
Bread 50  
5    
SAMPLE OUTPUT: 
142.5        
// number of item 
// item name and price of 1st item   
// item name and price of 1st item 
// discount % 
// total bill amount after applying discount  
(Total bill was 150 and discount % is 5 so total discount = 7.5. 
Final bill is 150 - 7.5 = 142.5)'''

n = int(input())
fruit_name = []
price_name = []

for i in range(1,n+1):
    name = input()
    price = int(input())
    fruit_name.append(name)
    price_name.append(price)

discount = int(input())
sum = 0

length = len(price_name)
for i in range(0,length):
    sum = sum + price_name[i]

discount_price = (sum * discount)/100

total = sum - discount_price
print(total)

