#Polymorphism

from Class import *


class Audi(Car):

    def __init__(self, wheels, doors, engine):
        super().__init__(wheels, doors, engine)

    def aboutCar(self):
        return "My " + self.__class__.__name__ + " is great, it can:"
    
    def accelerate(self):
        return self.__class__.__name__ + " -> Accelerate"

    def braking(self):
        return self.__class__.__name__ + " -> Brake"


car = Car(4, 4, "Xc75v")
print(car.aboutCar())
print(car.accelerate())
print(car.braking())
print()


opel = Opel(4, 4, "XAxZF")
print(opel.aboutCar())
print(opel.accelerate())
print(opel.braking())
print()


ford = Ford(4, 4, "XA2SF")
print(ford.aboutCar())
print(ford.accelerate())
print(ford.braking())
print()


honda = Honda(4, 4, "XA2SF")
print(honda.aboutCar())
print(honda.accelerate())
print(honda.braking())
print()


#Refactor - Inline
bmw = Car(4, 4, "KRSSF")
print(bmw.aboutCar())
print(bmw.accelerate())
print(bmw.braking())
print()


#Refactor - Move - Inner class
audi = Audi(4, 4, "ZX45F")
print(audi.aboutCar())
print(audi.accelerate())
print(audi.braking())
print()


# End of file
print()
input("Press Enter to continue...")