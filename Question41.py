'''CODING Total Price with Defaults

Problem Statement Define a function bill(price, qty=1, gst=18) that returns the total payable = price * qty * (1 + gst/100). Read three numbers: price, qty, gst. If qty is -1, use default 1. If gst is -1, use default 18. Print total rounded to 2 decimals.

Input One line: 
        three numbers price qty gst (integers)
Output One line:
        total (2 decimals)'''

def bill(price, qty = 1,gst = 18):
    if qty == -1:
        qty = 1
    if gst == -1:
        gst = 18

    total = price * qty * (1 + gst/100)
    return total

price = int(input("Enter price: "))
qty   = int(input("Enter qty: "))
gst   = int(input("Enter gst: "))

final_bill = bill(price,qty,gst)
print(f"{final_bill:.2f}") # 2 deminal tk answer ke liya

