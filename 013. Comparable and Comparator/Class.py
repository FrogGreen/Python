class Dog(object):

    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return ("\n||" + str(self.name) + ", " + str(self.color) + ", " + str(self.age) + "||")

    def __lt__ (self, other):
        if self.name == other.name:
            return self.age < other.age
        return self.name < other.name

    def __gt__ (self, other):
        return other.__lt__(self)