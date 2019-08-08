from abc import ABC, abstractmethod


class BaseCar(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(BaseCar):
    def __init__(self):
        self.__engine = 'V8'

    def stop(self):
        super().stop()

    def move(self):
        super().move()


a = Car()
