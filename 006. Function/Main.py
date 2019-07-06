# Function

# Calculate from celsius to kelvin
def celsiusToKelvin(celsius):
    return celsius + 273.15


# Calculate from kelvin to celsius
def kelvinToCelsius(kelvin):
    return kelvin - 273.15


# MainScope
print("0 Degree Celsius is:", celsiusToKelvin(0), "Kelvins,")
print("but 0 Kelvins is:", kelvinToCelsius(0), "Degree Celsius.")


# End of file
print()
input("Press Enter to continue...")