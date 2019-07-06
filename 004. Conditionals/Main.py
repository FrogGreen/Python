# Conditionals

# If statement
print("If statement:")
isRaining = True
skyIsCloudy = True
sunShines = True
temperature = 18

if(isRaining):
    print("You will need an umbrella")
elif(skyIsCloudy):
    print("It is possible to rain.")
else:
    print("Have a nice day")
if(isRaining & sunShines):
    print("Search for the rainbow")
print()


# Ternary operator
print("Ternary operator:")
ternaryOperator = "It's hot outside" if temperature > 19 else "It's cold outside"
print(ternaryOperator + "\n")


# Switch statement
print("Switch statement:")
accessCode = "000"
switcher = {
    "001":"Hello George!",
    "002":"Hello Stephen!",
    "003":"Hello Lucy!"
    }
print(switcher.get(accessCode,"Unauthorized access"))


# End of file
print()
input("Press Enter to continue...")