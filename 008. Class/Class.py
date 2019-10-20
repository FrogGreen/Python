class Car(object):

    def __init__(self, brand="", model="", numberVIN="", numberOfDoor=0):
        self.__brand = brand
        self.__model = model
        self.__numberVIN = numberVIN
        self._numberOfDoor = numberOfDoor

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def numberVin(self):
        return self.__numberVin

    @numberVin.setter
    def numberVin(self, value):
        self.__numberVin = value

    @property
    def numberOfDoor(self):
        return self.__numberOfDoor

    @numberOfDoor.setter
    def numberOfDoor(self, value):
        self.__numberOfDoor = value

    def __str__(self):
        return "Car: {" + "brand= " + self.__brand + ", model= " + self.__model + ", numberVIN= " + self.__numberVIN + ", numberOfDoor= " + str(self._numberOfDoor) + '}'