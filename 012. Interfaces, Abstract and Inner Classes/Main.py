#Interfaces, Abstract and Inner Class

from Class import *

nameToTest1 = ImplementationTwo()

nameToTest2 = ImplementationTwo().ImplementationThree()
nameToTest2.ImplementantionThree()
print()

nameToTest1.ImplementationOne()
print("Print1: ")
nameToTest1.print1()
print("Print2: ")
nameToTest1.print2()
print("Print3: ")
nameToTest1.print3()
print("Print4: ")
nameToTest1.print4()
print("Print5: ")
nameToTest1.print5()

print("\nPrint InterfaceOne: \n")
nameToTest1.print6()

print("\nPrint InterfaceTwo: \n")
nameToTest1.print7()

print("\nWe have also access to static method from interfaces in class:")
nameToTest1.print8()

print("\nWe have also access to variables in interfaces")
print(nameToTest1.interfaceOne)
print(super(ImplementationTwo, nameToTest1).interfaceTwo)

print("\nWe have also access to default method in interfaces")
print("InterfaceOne:")
print("Print1: ")
super(ImplementationTwo, nameToTest1).print1()
print("Print2: ")
super(ImplementationTwo, nameToTest1).print2()
print("Print3: ")
super(ImplementationTwo, nameToTest1).print3()
print("Print4: ")
super(ImplementationTwo, nameToTest1).print4(nameToTest1)
print("Print6: ")
super(ImplementationTwo, nameToTest1).print6()
print("\nInterfaceTwo:")
print("Print1: ")
InterfaceTwo.print1()
print("Print2: ")
super(ImplementationTwo, nameToTest1).print2()
print("Print7: ")
super(ImplementationTwo, nameToTest1).print7()

# End of file
print()
input("Press Enter to continue...")