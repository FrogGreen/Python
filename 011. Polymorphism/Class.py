class Car(object):

    def __init__(self, wheels, doors, engine):
        self.__wheels = wheels
        self.__doors = doors
        self.__engine = engine

    def aboutCar(self):
        return "My car is great, it can:"

    def accelerate(self):
        return "Car -> Accelerate"

    def braking(self):
        return "Car -> Brake"


class Ford(Car):

    def __init__(self, wheels, doors, engine):
        super().__init__(wheels, doors, engine)

    def aboutCar(self):
        return "My " + self.__class__.__name__ + " is great, it can:"

    def accelerate(self):
        return self.__class__.__name__ + " -> Accelerate"

    def braking(self):
        return self.__class__.__name__ + " -> Brake"


class Honda(Car):

    def __init__(self, wheels, doors, engine):
        super().__init__(wheels, doors, engine)

    def aboutCar(self):
        return "My " + self.__class__.__name__ + " is great, it can:"

    def accelerate(self):
        return self.__class__.__name__ + " -> Accelerate"

    def braking(self):
        return self.__class__.__name__ + " -> Brake"


class Opel(Car):

    def __init__(self, wheels, doors, engine):
        super().__init__(wheels, doors, engine)

    def aboutCar(self):
        return super(Opel, self).aboutCar() + "\nMy " + self.__class__.__name__ + " is great, it can:"

    def accelerate(self):
        return super(Opel, self).accelerate() + "\n" + self.__class__.__name__ + " -> Accelerate"

    def braking(self):
        return super(Opel, self).braking() + "\n" + self.__class__.__name__ + " -> Brake"