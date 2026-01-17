'''One sunny afternoon, a young student Manu sat at their computer, wondering if they were old enough to vote. They decided to ask their trusty program for the answer. "What is
your age?" the program asked. The student entered their age, hoping for an answer. The program thought for a moment and said, "If your age is 18 or older, you are eligible to
vote." The student waited nervously. If the number entered was 18 or more, the program would announce, "Eligible to vote!" But if it was less, it would respond with a simple, "Not
eligible to vote."
INPUT:
The program accepts a single integer input from the user, representing their age.
OUTPUT:
The program outputs one of two possible messages:
Eligible to vote. // if the age is greater than or equal to 18.
Not eligible to vote. // if the age is less than 18.
SAMPLE INPUT:
18
SAMPLE OUTPUT:
Eligible to vote'''

age = int(input())

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")