'''Q7.  Arctic Research Ice-Core Thermal Analyzer
In a remote Arctic research base, scientists study thermal readings from ice-core extraction machines.
These readings help determine melting patterns and hidden geothermal activity. But due to freezing
winds, sensor fogging, and device malfunctions, some values become corrupted. Each ice-core
machine records temperature readings in a tuple (integers or floats). However, the harsh environment
often causes invalid entries like text or unreadable symbols. Your task is to clean these readings and
figure out which machines show stable thermal output.
Your Task
Write a function analyze_icecore_thermal(thermal_data: list) -> tuple that:
Accepts a list of tuples, each containing temperature readings for one machine.
Example: [(155, 140.5, 133), (250, "GLITCH", 240), (95, 100, 102)]
For each tuple:
Ignore any invalid (non-numeric) entries.
Compute the average of only valid readings.
If the average is greater than 120, the machine is considered “stable.”
Collect the rounded integer averages of all stable machines and return them as a tuple.
Exception Handling Rules (exactly 2)
Use try–except to handle:
TypeError → if input is not a list → return "Invalid Data Type"
ValueError → if the list is empty → return "No Thermal Data Found"
Input Format
A list of tuples containing numeric or mixed-type thermal readings
Output Format
A tuple of integers representing the rounded average thermal readings of stable machines,
 or one of the error messages:
 "Invalid Data Type"
 "No Thermal Data Found"
Sample Input 1
[(155, 140.5, 133), (250, "GLITCH", 240), (95, 100, 102)]
Sample Output 1
(143, 245)
Sample Input 2
[]
Sample Output 2
No Thermal Data Found

OR

Q8.  Ancient Ruins Vibration Stability Detector
Archaeologists studying ancient ruins use vibration detectors to measure structural stability. But dust
storms, collapsed walls, and unstable ground often corrupt some recorded vibration values. Each
detector’s vibration data is stored as a tuple of readings (integers or floats). Sometimes, faulty sensors
capture invalid entries such as text or symbols. Your task is to clean these readings and determine
which ruins exhibit stable vibration patterns.
Your Task
Write a function detect_vibration_stability(vibes: list) -> tuple that:
Accepts a list of tuples, where each tuple contains vibration readings for a ruin section.
Example: [(160, 135.2, 128), (180, "NOISE", 190), (70, 85, 92)]
For each tuple:
Ignore any invalid (non-numeric) values.
Compute the average of valid readings.
If the average is greater than 120, the ruin section is considered “stable.”
Collect the rounded averages of all stable sections and return them as a tuple.
Exception Handling Rules (exactly 2)
Use try–except to handle:
TypeError → if input is not a list → return "Invalid Data Type"
ValueError → if the list is empty → return "No Vibration Data Found"
Input Format
A list of tuples containing numeric or mixed-type vibration readings
Output Format
A tuple of integers representing the rounded average vibration readings of stable ruin sections,
 or one of the error messages:
 "Invalid Data Type"
 "No Vibration Data Found"
Sample Input 1
[(160, 135.2, 128), (180, "NOISE", 190), (70, 85, 92)]
Sample Output 1
(141, 185)
Sample Input 2
12345
Sample Output 2
Invalid Data Type

OR

Q9.  Space Station Oxygen Module Stability Scanner
On an orbital research station, engineers constantly monitor oxygen module output levels to ensure the
crew’s safety. However, cosmic dust, micro-meteor impacts, and sensor glitches sometimes corrupt the
readings. Each module’s oxygen output is recorded as a tuple containing readings (integers or floats).
Occasionally, the system mistakenly logs invalid values such as text or special characters. Your task is
to filter corrupted values and determine which oxygen modules are functioning stably.
Your Task
Write a function scan_oxygen_modules(modules: list) -> tuple that:
Receives a list of tuples, where each tuple stores oxygen output readings for one module.
Example: [(145, 138.4, 129), (260, "BAD", 255), (110, 115, 118)]
For each tuple:
Ignore all non-numeric values.
Compute the average of valid readings.
If the average is greater than 120, the module is labeled “stable.”
Gather the rounded averages of all stable modules and return them as a tuple.
Exception Handling Rules (exactly 2)
Use try–except to handle:
TypeError → input is not a list → return "Invalid Data Type"
ValueError → list is empty → return "No Oxygen Data Found"
Input Format
A list of tuples containing numeric or mixed-type oxygen output readings
Output Format
A tuple of integers representing the rounded average output of stable oxygen modules,
 or one of the error messages:
 "Invalid Data Type"
 "No Oxygen Data Found"
Sample Input 1
[(145, 138.4, 129), (260, "BAD", 255), (110, 115, 118)]
Sample Output 1
(137, 258)
Sample Input 2
[]
Sample Output 2
No Oxygen Data Found'''

num = eval(input())

try:
    if not isinstance(num, list):
        raise TypeError

    if len(num) == 0:
        raise ValueError

    final = []
    for number in num:
        total = 0
        count = 0
        for j in number:
            if isinstance(j, (int, float)):
                total = total + j
                count += 1

        if count > 0:
            avg = total / count
            if avg > 120:
                final.append(round(avg))
    print(tuple(final))

except ValueError:
    print("No Thermal Data Found")

except TypeError:
    print("Invalid Data Type")