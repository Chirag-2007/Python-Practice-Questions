'''Q 1. At "PizzaHut," customers can order pizzas with various toppings. The price of each pizza is 
determined by its size and the number of toppings. Write a Python program that helps calculate the 
total cost of a pizza order. 
Your program should implement the following: 
Define a function called calculate_pizza_cost that takes two arguments: 
size: The size of the pizza ("small," "medium," or "large"). 
toppings: The number of toppings the customer wants on the pizza (an integer). 
Inside the function, set the base price for each pizza size: 
Small: $10 
Medium: $15 
Large: $20 
Calculate the total cost by adding the base price and the cost of toppings. Each topping costs $2. 
Display the size of the pizza, the number of toppings, the total cost, and a thank you message. 
Sample Input 1: 
Small                                              
2                                                      
Sample Output 1: 
Small                                                                                        
2                                                                                              
$14                                                                                          
//Enter the size of the pizza (small/medium/large)  
//Enter the number of toppings 
Thank you for ordering from PizzaHut!                       
Sample Input 2: 
Large            
5                            
Sample Output 2: 
Large                                                                                             
5                                                                                                      
$30                                                                                                   
Thank you for ordering from PizzaHut!                                
//Size of Pizza  
//Number of Toppings 
//Total Cost 
// thank you message 
//Enter the size of the pizza (small/medium/large) 
//Enter the number of toppings 
//Size of Pizza 
//Number of Toppings 
//Total Cost 
// thank you message'''

def calculate_pizza_cost(size,topping):
    size = size.lower()
    if size == "small":
        cost = 10 + (2*topping)
    elif size == "medium":
        cost = 15 + (2*topping)
    elif size == "large":
        cost = 20 + (2*topping)
    else:
        print("Invalid pizza size!")
        return None
    return cost

size = input()
topping = int(input())
print(size)
print(topping)
print(f"${calculate_pizza_cost(size,topping)}")
print("Thank you for ordering from PizzaHut!")
