'''The bank is flooded with thousands of loan applications every day. Employees are struggling with the paperwork, and frustrated customers are lining up in long queues. To speed things up, the bank decides to automate the loan approval process. But the applicants don’t always cooperate:

Some type their age as negative numbers like -5, or even unrealistic values like 200.
Some type their age or credit score as words like “twenty-five” instead of numbers.
Some submit a credit score of 0 or leave it blank, hoping the system won’t notice.

The bank has clear rules for automation:
1. Applicant must be at least 21 years old.
2. Applicant must have a credit score greater than 700.
3. If any invalid data (negative, zero, or text) is entered → the system should output “Invalid input”.

You need to write the program that will help the bank decide whether the loan is approved,
rejected, or invalid. Decision Rules:
- If invalid → print “Invalid input”
- If not eligible → print “Loan Rejected”
- Else → print “Loan Approved”
'''

# IMPORTANT QUESTION -->

age_str = input()
credit_score_str = input()

if not age_str.isdigit() or not credit_score_str.isdigit():
    print("Invalid input")
else:
    age = int(age_str)
    credit_score = int(credit_score_str)

    if age <= 0 or credit_score <= 0:
        print("Invalid input")
    elif age < 21 or credit_score <= 700:
        print("Loan Rejected")
    else:
        print("Loan Approved")