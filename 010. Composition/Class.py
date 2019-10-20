class Engine(object):

    def __init__(self, percentOfMaxSpeed=0, horsePower=0, cylinders=0, valve=0, isOn=False):
        self.__percentOfMaxSpeed = percentOfMaxSpeed
        self.__horsePower = horsePower
        self.__cylinders = cylinders
        self.__valve = valve
        self.__isOn = isOn

    def isOn(self):
        return "Engine is on" if self.__isOn else "Engine stop"
    
    def start(self):
        self.__isOn = True

    def stop(self):
        self.__isOn = False


class Gearbox(object):

    def __init__(self, rpm=0, transmission=1, maxGear=3, currentGear=0):
        self.__rpm = rpm
        self.__transmission = transmission
        self.__maxGear = maxGear
        self.__currentGear = currentGear


class Vehicle(object):

    def __init__(self, wheel, weight):
        self.__wheel = wheel
        self.__weight = weight


class Car(Vehicle):

    def __init__(self, wheel, weight, door, gearbox, engine):
        super().__init__(wheel, weight)
        self.__door = door
        self.__gearbox = gearbox
        self.__engine = engine

    def carStart(self):
        self.__engine.start()
        self.__engine._Engine__percentOfMaxSpeed = 5
        self.__engine.isOn()
        self.__gearbox._Gearbox__rpm = 750
        self.__gearbox._Gearbox__currentGear = 0

    def carStop(self):
        self.__engine.stop()
        self.__engine._Engine__percentOfMaxSpeed = 0
        self.__engine.isOn()
        self.__gearbox._Gearbox__rpm = 0
        self.__gearbox._Gearbox__currentGear = 0

    def changeSpeed(self, accelerate):
        if (self.__engine._Engine__percentOfMaxSpeed + accelerate > 100 or self.__engine._Engine__percentOfMaxSpeed + accelerate < 0):
            print("Speed change impossible")
        else:
            self.__engine._Engine__percentOfMaxSpeed = self.__engine._Engine__percentOfMaxSpeed + accelerate
            self.__gearbox._Gearbox__currentGear = self.__gearbox._Gearbox__currentGear * self.__engine._Engine__percentOfMaxSpeed / 100
            #If Current gear is equal to 0, Car stop
            if ((self.__gearbox._Gearbox__currentGear * self.__gearbox._Gearbox__transmission) == 0):
                self.__engine.stop()
            else:
                self.__gearbox._Gearbox__rpm = (self.__engine._Engine__percentOfMaxSpeed * 1500 / (self.__gearbox._Gearbox__currentGear * self.__gearbox._Gearbox__transmission))

    def carParameter(self):
        self.__engine.isOn()
        print("RPM: " + str(self.__gearbox._Gearbox__rpm))
        print("Current Gear: " + str(self.__gearbox._Gearbox__currentGear))
        print("Current Speed: " + str(self.__engine._Engine__percentOfMaxSpeed) + "%.")