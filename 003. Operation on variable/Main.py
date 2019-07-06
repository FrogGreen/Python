# Operation on variable

name = "FrogGreen"


# STRINGS
print("STRINGS")
print('This is what is going on, when you use single quotes')  # Using single quotes ('')
print("This is what is going on, when you use double quotes")  # Using double quotes ("")
print("FrogGreen has got: " + str(len(name)) + " characters")
print(name.upper())  # Make all characters Upper
print(name.lower())  # Make all characters Lower
print(name + " is starting programming in python/n")

# Printing in multiple lines
print("""
{} can also print text
in multiple lines,
he knows how to do it/n
""".format(name))

# String indexing
print("First character of " + name + " is: " + name[0])
print("Fourth character of " + name + " is: " + name[3])
print("Last character of " + name + " is: " + name[-1])
print("Third-last character of " + name + " is: " + name[-3])
print("Character from first (included) to third (excluded) of " + name + " is: " + name[:2])
print("Character from second (included) to fifth (excluded) of " + name + " is: " + name[1:4])
print("Character from fourth (included) to last (included) of " + name + " is: " + name[3:])
print("Characters from the third-last (included) to the end (included) of " + name + " is: " + name[-3:])
print("Characters from the first (included) to the third-last (excluded)of " + name + " is: " + name[:-3] + "/n")


# NUMBERS
print("NUMBERS:")
print("4+3 is: " + str(4 + 3))  # Addition - 7
print("5-2 is: " + str(5 - 2))  # Subtraction - 3
print("6*8 is:" + str(6 * 8))  # Multiplication - 48
print("42|8 is: " + str(42 % 8))  # Modulo - 2
print("43/2 is: " + str(43 / 2))   # Division - 21.5
print("but 43//2 is: " + str(43 // 2))  # Division - 21
print("2^7 is: " + str(2 ** 7))  # Powers - 128


# End of file
print()
input("Press Enter to continue...")