'''Q 1. Problem Statement 
You are managing a parking lot, and you need to calculate the total parking fee for vehicles based on the time they spend in the lot. The parking lot charges fees based on the following structure:
•	The first 2 hours are free.
•	After the first 2 hours, the parking fee is Rs 20 per hour.
•	The maximum fee a vehicle can be charged in a day (24 hours) is Rs 100.
Write a function calculate_parking_fee(hours) that calculates the total fee based on the number of hours the vehicle has been parked.
•	If the hours parked are less than or equal to 2, the fee is Rs 0.
•	For hours greater than 2, calculate the fee by charging Rs 10 per hour starting from the 3rd hour.
•	If the fee exceeds Rs 100, it should be capped at Rs 100.
Explanation:
1.	Parked for 1 hour: Since it's less than 2 hours, the parking is free.
2.	Parked for 2 hours: Exactly 2 hours means no fee.
3.	Parked for 3 hours: The first 2 hours are free, so the fee for the 3rd hour is Rs 10.
4.	Parked for 10 hours: After the first 2 free hours, there are 8 chargeable hours. The fee is Rs 10 per hour, so the total fee is Rs 80.
5.	Parked for 24 hours: Even though the total fee without a cap would be higher than Rs 100, the fee is capped at Rs 100.
Constraints: 0 <= hrs 

Input Format:
Input contains the value of hrs in integer (for e.g. 10)

Output Format:
Prints the result in amount in integer (for e.g. 80) ma code bejta hu bhai tu chrck kariyo mera code  '''

n = int(input())

if n <= 2:
    price = 0
else:
    price = (n - 2) * 10
    if price > 100:
        price = 100

print(price)