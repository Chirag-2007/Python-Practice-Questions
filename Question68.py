'''You are appointing as Computer Programmer in Cameron Hotel, Chandigarh. A task is given to you for generate a WiFi password for new customer who book a room in a hotel. A customer registration will contain Customer First Name and Room No. Instructions for generating a WiFi password as:
1.	Your password is of 4 digits long only.
2.	Unit digit will be alphabeting character (lower case) that will have calculated by the length of customer first name.
3.	Tenth digit will be sum of customer room no. Keep summation until reach at single digit.
4.	Hundreds digit will be special character (! ,@,#,$,%,^,&,*,(,) ) calculate by the sum of Room No. Keep summation until reach at single digit. 
5.	Thousands unit will be numeric calculated on basis of sum of room number as follows. Keep summation until reach at single digit. 
a.	If sum is odd, then same number will be allocated.
b.	If sum is even, then adding one digit to the result.
Input Format: 
Customer Name: James Gosling, Room No: 312
Output Format:
WiFi Password: 7^6e

Hidden Test case 1 - (Easy) Weightage 20%
Input
Larry Page, Room No: 278

Output
WiFi Password: 9*8e

Hidden Test case 2 - (Easy) Weightage 20%
Input
Rattan Tata, Room No: 142

Output
WiFi Password: 7&7f

Hidden Test case 3 - (Easy) Weightage 20%
Input
Azim Premji, Room No: 511

Output
WiFi Password: 7&7d

Hidden Test case 4 - (Easy) Weightage 20%
Input
Sachin Tendulkar, Room No: 220

Output
WiFi Password: 4$4f

Hidden Test case 5 - (Easy) Weightage 20%
Input
Virat Kohli, Room No: 652

Output
WiFi Password: 5@2e'''

def digit_sum(num):
    while num > 9:
        total = 0
        while num > 0:
            last_digit = num % 10
            total = total + last_digit
            num = num // 10
        num = total
    return num

name = input("Customer Name: ")
name_arr = name.split()
room_no = int(input("Room No: "))

length = len(name_arr[0])
unit_digit = chr(96 + length)

sum_room = digit_sum(room_no)
tens_digit = sum_room

if sum_room % 2 == 0:
    thousand_digit = sum_room + 1
else:
    thousand_digit = sum_room

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
hundred_digit = special_chars[sum_room - 1]

password = str(thousand_digit) + hundred_digit + str(tens_digit) + unit_digit
print("WiFi Password:",password)



