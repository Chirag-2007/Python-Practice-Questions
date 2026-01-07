# Q16. Global vs Local Variable Demo (Scope Rules)

counter = 0

def increment():
    global counter
    counter += 1
    print(counter)

increment()
increment()
increment()

# Q17. Factorial Using Recursion

def  factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial(n-1)
    
n = int(input())
print(factorial(n))

# Q18. Double Using Lambda

double = lambda x: 2 * x

n = int(input())
print(double(n))

# Q19. Sum of List Elements (Passing List to Function)

def list_sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

n = int(input())
num = list(map(int,input().split()))
print(list_sum(num))

# Q20. List Statistics (Indexing and Slicing)

n = int(input())
num = list(map(int,input().split()))

first_element = num[0]
last_element = num[n-1]
middle_element = num[1:n-1]

print(first_element)
print(last_element)
for i in middle_element:
    print(i,end=" ")