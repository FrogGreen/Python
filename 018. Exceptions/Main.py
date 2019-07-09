# Exceptions

# Using LBYL (Look Before You Leap)
def divideFirstMethod(x, y):
    if (y != 0):
        return x / y
    else:
        return 0


# Using EAFP (Easier to Ask Forgiveness than Permission):
def divideSecondMethod(x, y): 
    try:
        return x / y
    except:
        return 0


# Throw new Arithmetic Exception
def divideThirdMethod(x, y): 
    try: 
        return x / y
    except ZeroDivisionError as e:
        print("Did you try to divide by zero? {}".format(e))


# Not using exceptions
def divide(x, y):
    return x / y


# Value
x = 45
y = 35
z = 0


# Exception handle
try:
    print(str(x) + "/" + str(y) + "is:")
    print(divideFirstMethod(x, y))
    print(divideSecondMethod(x, y))
    print(divideThirdMethod(x, y))
    print(divide(x, y))

    print(str(x) + "/" + str(z) + "is:")
    print(divideFirstMethod(x, z))
    print(divideSecondMethod(x, z))
    print(divideThirdMethod(x, z))
    print(divide(x, z))
    a = 0 / 0
except ZeroDivisionError as e:
    print(e)
    print("Something went wrong, isn't it?")
finally:
    print("Well done! You did it! Program still work, no error crash!")


# End of file
print()
input("Press Enter to continue...")