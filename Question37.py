# Problem: City bus fare per ride depends on age:
# - Age < 5 → 0 (free)
# - Age 5–17 → 10
# - Age 18–59 → 20
# - Age ≥ 60 → 12
# Given age and rides (number of rides), compute total fare as integer.
# If age or rides is negative, print "INVALID".

age = int(input())
rides = int(input())

if age < 0 or rides < 0:
    print("INVALID")
elif age < 5:
    fare = 0 * rides
    print(fare)
elif age <= 17:
    fare = 10 * rides
    print(fare)
elif age <= 59:
    fare = 20 * rides
    print(fare)
else:
    fare = 12 * rides
    print(fare)