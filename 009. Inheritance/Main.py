#Inheritance

from Class import Home
from Class import House
from Class import Flat


#Creating new Home
myFirstHome = Home(10, 2, 1, 2)


#Creating new House
myFirstHouse = House(10, 3, 1, 2, 3)


#Creating new Flat
myFirstFlat = Flat(3, 2, 1, 1, 1)


#Implicit casting Home
mySecondHome = Home(House(10, 3, 1, 2, 2))
myThirdHome = Home(Flat(3, 2, 1, 1, 1))


#Override method toString
print(myFirstHome)
print(myFirstHouse)
print(myFirstFlat)
print(mySecondHome)
print(myThirdHome)


#Override method myPlaceToLive
myFirstHome.myPlaceToLive()
mySecondHome.myPlaceToLive()


#Method checkCarInGarage
myFirstHouse.checkCarInGarage()
(House(mySecondHome)).checkCarInGarage()


# End of file
print()
input("Press Enter to continue...")