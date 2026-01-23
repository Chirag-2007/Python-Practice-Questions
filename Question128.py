'''Grade of a student

Based on the marks obtained by a student in five different subjects, calculate total marks and average of marks in five subjects. Display total marks, average and grade of student. The grade of student is displayed based on the average as follows:

Grade is A – if average >= 75
Grade is B – if average >= 60 and < 75
Grade is C – if average >= 55 and < 60
Grade is D – if average >= 50 and < 55
Grade is E – if average < 50

Also if total marks are zero then display message "FAILED".

Sample Input 1:
23 // marks obtained in subject 1
78 // marks obtained in subject 2
90 // marks obtained in subject 3
45 // marks obtained in subject 4
67 // marks obtained in subject 5'''

sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = int(total / 5)
print(total)
print(avg)

if total == 0:
    print("FAILED")
else:
    if avg >= 75:
        print("GRADE A")
    elif avg >= 60 and avg < 75:
        print("GRADE B")
    elif avg >= 55 and avg < 60:
        print("GRADE C")
    elif avg >= 50 and avg < 55:
        print("GRADE D")
    else:
        print("GRADE E")