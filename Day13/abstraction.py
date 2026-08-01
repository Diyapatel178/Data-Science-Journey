from abc import ABC , abstractmethod

class vehicals(ABC):

    @abstractmethod
    def Start(self):
        pass
class car(vehicals):

    def Start(self):
        print("car started")

car = car()
car.Start()

