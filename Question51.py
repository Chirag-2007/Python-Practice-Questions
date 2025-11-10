'''5.Calculation 
Aditi and Abhay donot like maths, they find it difficult to remember the formulas of area and 
perimeter of different shapes. So they want to design a system which can calculate the area 
and perimeter of different shapes. Help them to do so. 
Write a program to create two classes’ area and perimeter having functions to calculate and 
print the area and perimeter of square, rectangle and circle when the dimensions are passed as 
argument to the function.  
NOTE - for circle, use pi as 3.14
Input Format 
The first line of input contains the name of shape(in lower case)   
The second line contains the dimension of shape to calculate the area and perimeter. 
Output Format 
The first line should print the area of the shape and second line should print the perimeter of 
the shape.  Print the result upto two decimal places. 
SAMPLE INPUT: 
circle // name of shape  
3.5
// dimension (circle - radius) 
SAMPLE OUTPUT: 
39.2343    
21.98 
// area 
// perimeter'''

def circle(n):
    pi = 3.14
    print("Area:",pi *(n**2))
    print("Perimeter:",2 * pi * n)


def square(n):
    print("Area:",n*n)
    print("Perimeter:",4*n)


def rectangle(m,n):
    print("Area:",m*n)
    print("Perimeter:",2*(m + n))

shape = input()

if shape == "circle":
    radius = float(input())
    circle(radius)

elif shape == "square":
    side = float(input())
    square(side)

elif shape == "rectangle":
    length = float(input())
    breadth = float(input())
    rectangle(length, breadth)




