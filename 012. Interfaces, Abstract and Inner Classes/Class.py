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