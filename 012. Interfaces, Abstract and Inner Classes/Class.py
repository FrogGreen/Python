from abc import ABC, abstractmethod

class InterfaceOne(object):

    interfaceOne = "InterfaceOne - > Interface allow to have constant variables"

    def InterfaceOne(self):
        return self.interfaceOne

    @classmethod
    def print1(self):
        print("InterfaceOne - > This is the different between DEFAULT and abstract method")

    @classmethod
    def print2(self):
        print("InterfaceOne - > This is the different between DEFAULT and default")

    @classmethod
    def print3(self):
        print("InterfaceOne - > This is the different between DEFAULT and static")

    @staticmethod
    def print4(self):
        print("InterfaceOne - > This is the different between STATIC and static")

    @classmethod
    def print6(self):
        print(self.InterfaceOne(self))
        self.print1(self)
        self.print2(self)
        self.print3()
        self.print4(self)


class InterfaceTwo(object):

    interfaceTwo = "InterfaceTwo - > Interface allow to have constant variables"

    def InterfaceTwo():
        return "InterfaceTwo - > We can use interface method as private"

    def print1():
        pass

    @classmethod
    def print2():
        print("InterfaceTwo - > This is the different between default and DEFAULT")

    @staticmethod
    def print3():
        print("InterfaceTwo - > This is the different between default and STATIC")

    @staticmethod
    def print4():
        print("InterfaceTwo - > This is the different between static and STATIC")

    @staticmethod
    def print5():
        print("InterfaceTwo - > This is the different between abstract and STATIC")

    @classmethod
    def print7(self):
        print(self.InterfaceTwo())
        self.print1(self)
        self.print2(self)
        self.print3()
        self.print4(self)
        self.print5(self)


class ImplementationOne(object):

    @abstractmethod
    def ImplementationOne(self):
        pass


class ImplementationTwo(ImplementationOne, InterfaceOne, InterfaceTwo):

    interfaceTwo = "We can also override constant variables"

    def ImplementationOne(self):
        print(InterfaceOne.interfaceOne)
        print(InterfaceTwo.interfaceTwo)

    def print1(self):
        print("Implementation Two - > If we have default and abstract method, we have to override it, becaue we have to implement abstract")

    def print2(self):
        print("Implementation Two - > If we have two default method, we have to override it, becaue we have to decide which one is the most important")

    def print4(self):
        print("Implementation Two - > We have two static method")

    def print5(self):
        print("Implementation Two - > We have static and abstract method")

    def print8(self):
        InterfaceOne.print4(self)
        InterfaceTwo.print3()
        InterfaceTwo.print4()
        InterfaceTwo.print5()

    class ImplementationThree:

        def ImplementantionThree(self):
            print("We can have class in class, that call inner class")
    