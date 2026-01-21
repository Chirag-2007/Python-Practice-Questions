'''Factory Production Output

A factory floor generates production reports by shift. Reports map Machine ID to the Units Produced. Some units are marked "scrapped" instead of an integer count.

You must:

Sum the Total Units Produced for each Machine ID.

If the production count is not an integer, skip that entry and print
"Production data error, invalid unit count".

Display the total units produced per machine.

Input Format:
A list of dictionaries:
[{ Machine ID : Units }, …]

Output Format:
A single dictionary with values:
{ Machine ID : Total Units, … }

Sample Input 1:
[{'M01': 100}, {'M02': 200}, {'M01': 50}]

Sample Output 1:
{'M01': 150, 'M02': 200}

Sample Input 2:
[{'M03': 300, 'M04': 100}, {'M03': 'scrapped', 'M05': 50}]

Sample Output 2:
Production data error, invalid unit count
{'M03': 300, 'M04': 100, 'M05': 50}'''

def manage_production_output(reports):
    result = {}

    for record in reports:
        for machine, units in record.items():
            if type(units) != int:
                print("Production data error, invalid unit count")
                continue
            if machine in result:
                result[machine] += units
            else:
                result[machine] = units
    return result

reports = eval(input()) # eval() ek built-in function hai jo string ko Python expression me convert karke execute karta hai.
print(manage_production_output(reports))
