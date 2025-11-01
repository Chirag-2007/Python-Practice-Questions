# LCM of 2 numbers
''' FORMULA -> LCM(x,y)=x * y / GCD(x,y)'''

x = int(input())
y = int(input())
gcd = 1

for i in range(1,min(x,y)+1):
    if x % i == 0 and y % i == 0:
        gcd = i
        
lcm = x * y // gcd # ya formula yaad rakhna h
print(lcm)
