# Lists, Tuples, Sets, Dictionary

# 1D Lists
print("1D lists:")
days = []
number = ["1", "2", "3", "4", "5", "6", "7"]

# Add some elements
days.append("Monday")
days.append("Tuesday")
days.append("Wednesday")
days.append("Thursday")
days.append("Friday")
days.append("Saturday")
days.append("Sunday")

for i in range(len(number)):
    print("#" + number[i] + ". day of week is: " + days[i])

# Check if May is name of week day
print("Is May is name of week day? " + str("May" in days))


# 2D lists
print("\n2D lists:")
grade = [[3, 4.5, 5, 3.5],
            [5, 5, 5, 5, 5],
            [1, 1, 2, 3, 2, 3],]

sum = 0
average = 0
gradeNumber = 0

for j in range(len(grade)):
    for k in range(len(grade[j])):
        sum, gradeNumber = sum + grade[j][k], gradeNumber + 1

average = sum / gradeNumber
print(average)


# Tuples
print("\nTuples:")
location = (13.4125, 103.866667)
print("\nLatitude:", location[0])
print("Longitude:", location[1])

dimensions = 165, 14, 25
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))


# Sets
print("\nSets:")
carNumber = set()
carNumber.add("KMO5567")
carNumber.add("SDF9538")
carNumber.add("FGV9234")
carNumber.add("XCVG432")
carNumber.add("XCV4321")
carNumber.add("XCV2587")
carNumber.add("AAA6543")
carNumber.add("XCV4321")
carNumber.add("XCV2587")
carNumber.add("AAA6543")
print("Here is list of car number: " + str(carNumber))

carNumber.pop()
print("Here is list of car number after pop: " + str(carNumber))

if "XCVG432" in carNumber:
    carNumber.remove("XCVG432")
    print("Here is list of car number after remove \"XCV4321\": " + str(carNumber))


# Dictionary
print("\nDictionary:")
cars = {}
cars["NISSAN"] = 35
cars.update({"OPEL": 43})
cars.update({"BMW": 39})
cars.update({"BENTLEY": 43})
cars.update({"HONDA": 15})

for key, val in cars.items():
    print("Found total {} {} cars!".format(key, val))


# End of file
print()
input("Press Enter to continue...")