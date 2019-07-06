# Loops

numberOfSign = 50
number = 0
alarmBeep = True


# For loop
print("For loop:")
print("Warning number from 0 to 4:")
for i in range(5):
    print("Warning number #" + str(i))
print()

print("Warning number from 5 to 7:")
for i in range(5, 8):
    print("Warning number #" + str(i))
print()

print("Warning number from 8 to " + str(numberOfSign) + " every 7:")
for i in range(8, numberOfSign + 1, 7):
    print("Warning number #" + str(i))
print()


# While loop with break
print("While loop:")
while(alarmBeep == True):
    number += 5
    if(number >= numberOfSign):
        break
    print("Alarm number #",number)
print()


# For loop with continue keyword
print("Continue keyword:")
for i in range(0, 4):
    for j in range(0, 4):
        if (i == j):
            continue
        print("Caution, number of error #" + str(i) + str(j))
print()


# For loop with break keyword
print("Break keyword:")
for i in range(0, 4):
    for j in range(0, 4):
        if (i == j):
            break
        print("Caution, number of error #" + str(i) + str(j))
print()


# End of file
print()
input("Press Enter to continue...")