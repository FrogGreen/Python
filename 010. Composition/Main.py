#Composition

from Class import Engine
from Class import Car
from Class import Gearbox


kyr435 = Engine(horsePower=450, cylinders=4, valve=16)
honda = Car(4, 1050, 4, Gearbox(transmission=20, maxGear=5), kyr435)

honda.carStart()
honda.carParameter()
honda.changeSpeed(15)
honda.carParameter()
honda.changeSpeed(75)
honda.carParameter()


# End of file
print()
input("Press Enter to continue...")