# Class

from Car import Car


#Creating new object Mazda RX
mazdaRX = Car()
mazdaRX.brand ="Mazda"
mazdaRX.model="RX"
mazdaRX._Car__numberVIN = "WXYZ6324"
mazdaRX._numberOfDoor = 4


#Creating new object Ford Focus
fordFocus = Car("Ford", "Focus", "WX0Y6234", 4)


#Printing information about these object
print(mazdaRX)
print(fordFocus)


# End of file
print()
input("Press Enter to continue...")