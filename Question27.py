# Neha receives her monthly electricity bill.
# Rules: First 100 units @ Rs 5/unit; Next 100 units @ Rs 7/unit; Beyond 200 units @ Rs 10/unit

n = int(input("Enter number of units: "))
if n <= 100:
    bill = 5 * n
elif n <= 200:
    bill = (5 * 100) + (n - 100) * 7
else:
    bill = (5 * 100) + (7 * 100) + (n - 200) * 10

print("Monthly bill:",bill)