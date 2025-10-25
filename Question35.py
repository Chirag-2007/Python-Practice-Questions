# Sum and Average

n = int(input("Enter n: "))
sum = 0
marks_list = []

for i in range(1,n+1):
    marks = int(input("Enter marks: "))
    sum = sum + marks
    marks_list.append(marks)

average = sum / n
print("Average of marks obtained by student is:",average)

marks_list.sort()
max_mark = marks_list[n-1]

print("Highest marks obtained by student is:",max_mark)


