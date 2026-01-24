'''Inventory Shipment Tally

A warehouse tracks incoming inventory using manifests. Each manifest is a dictionary mapping Product Code Name to the Shipped Quantity. Multiple manifests often contain duplicate codes, and occasionally, quantity is logged incorrectly as text.

You must:

Calculate the Total Shipped Quantity for each Product Code.

Invalid quantity entries (non-integers) must be skipped with a warning message
"Non-integer quantity skipped".

Output the combined product inventory.

Input Format:

A list of dictionaries:
[{ Code Name : Quantity }, ...]

Output Format:

A single dictionary with values:
{ Code Name : Total Quantity }

Sample Input 1:
[{'PZ1': 50}, {'PZ2': 100}, {'PZ1': 20}]

Sample Output 1:
{'PZ1': 70, 'PZ2': 100}'''

def manage_inventory_shipments(inventory_records):
    result = {}

    for record in inventory_records:
        for name, quantity in record.items():
            if type(quantity) != int:
                print("Non-integer quantity skipped")
                continue
            if name in result:
                result[name] += quantity
            else:
                result[name] = quantity

    return result

record = eval(input())
print(manage_inventory_shipments(record))