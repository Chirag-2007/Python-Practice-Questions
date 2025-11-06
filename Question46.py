# Sorting of list without using sort function -> Important Question

num = [1,7,2,5,9]
length = len(num)

for i in range(0,length):
    for j in range(i+1,length):
        if num[j] < num[i]:
            # Swap of 2 numbers
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)


