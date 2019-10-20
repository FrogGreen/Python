class Home(object):

    def __init__(self, window=0, room=0, bathroom=0, bed=0):
        self.__window = window
        self.__room = room
        self.__bathroom = bathroom
        self.__bed = bed

    def __str__(self):
        return "Home{" + "window=" + str(self.__window) +", room=" + str(self.__room) +", bathroom=" + str(self.__bathroom) +", bed=" + str(self.__bed) +'}'
    
    def myPlaceToLive(self):
        print("I like my " + str(self))


class House(Home):

    def __init__(self, window = 0, room = 0, bathroom = 0, bed = 0, carInGarage = 0):
        super().__init__(window, room, bathroom, bed)
        self.__carInGarage = carInGarage
    
    def __str__(self):
        return super(House, self).__str__() + " House{" + "carInGarage=" + str(self.__carInGarage) + '}'
    
    def myPlaceToLive(self):
        super(House, self).myPlaceToLive()
        print("My house is so cool")

    def checkCarInGarage(self):
        print("Is car in garage?" + " Yes, there are " + str(self.__carInGarage) + " car in garage.")


class Flat(Home):

    def __init__(self, window = 0, room = 0, bathroom = 0, bed = 0, carPark = 0):
        super().__init__(window, room, bathroom, bed)
        self.__carPark = carPark
    
    def __str__(self):
        return super(Flat, self).__str__() + " Flat{" + "carPark=" + str(self.__carPark) + '}'