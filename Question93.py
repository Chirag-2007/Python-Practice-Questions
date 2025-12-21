# Topic 2: map, filter & reduce Functions 

# Q1: Curved Scores — Map, Filter Pipeline

num = list(map(int,input().split()))

if any(x < 0 or x > 100 for x in num):
    print("Invalid input")
else:
    more_40 = list(filter(lambda x: x >= 40,num))
    add_5 = list(map(lambda x: min(x + 5, 100), more_40))  # agar x + 5, 100 se zyada ho jaye, to 100 hi lega
    print(add_5)

# Q2: Prime Filter — Keep Only Primes

num = list(map(int,input().split()))
prime_arr = []

for i in num:
    prime_num = True
    if i < 2:
        prime_num = False
    else:
        for j in range(2,i):
            if i % j == 0:
                prime_num = False
                break
        if prime_num == True:
            prime_arr.append(i)

print(prime_arr)

# Q3: Product of Non-Zero Digits — Reduce

from functools import reduce
num_str = input()

filter_non_zero = list(filter(lambda x: int(x) != 0,num_str))

product = reduce(lambda x,y: int(x)*int(y),filter_non_zero)
print(product)

# Q4: Normalize Names — Map & Filter

name= list(input().split())

name_1 = list(map(lambda x: x.replace('_',' '),name))
upper_name = list(map(lambda x: x.strip().title(),name_1))

length_more_3 = list(filter(lambda x: len(x) >= 3,upper_name))
print(length_more_3)

# Q5: Sales Summary — Reduce with Aggregation

num = list(map(int,input().split()))
sum = 0

for i in num:
    sum = sum + i

sorted_num = sorted(num)
length = len(sorted_num)
print("Total:",sum)
print("Max:",sorted_num[length-1])
print("Min:",sorted_num[0])

        


    


