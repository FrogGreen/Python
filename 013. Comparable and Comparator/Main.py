#Comparable and Comparator

from Class import Dog
from operator import itemgetter, attrgetter


#List
print("List\n")
dog = []
dog.append(Dog("Klavi", "Brown", 4))
dog.append(Dog("Ornim", "Black", 5))
dog.append(Dog("Alvin", "Brown", 3))
dog.append(Dog("Lessie", "White", 2))
dog.append(Dog("Bambi", "Black", 3))


#Default list order
print("Default order of Dog list:\n")
print(*dog)


#Name sorted list order
dog.sort()
print("\nName order of Dog list:\n")
print(*dog)


#Age sorted list order
#If same age sort by name
dog=sorted(dog,key=lambda dog: dog.age,reverse=False)
print("\nAge order of Dog list:\n")
print(*dog)


#Color sorted list order
dog=sorted(dog, key=attrgetter('color'),reverse=False)
print("\nColor order of Dog list:\n")
print(*dog)


#Age sorted list order
#If same age sort by color
dog=sorted(dog,key=lambda dog: (dog.age, dog.color),reverse=False)
print("\nAge order of Dog list:\n")
print(*dog)


# End of file
print()
input("Press Enter to continue...")