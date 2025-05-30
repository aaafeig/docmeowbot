from abc import ABC, abstractmethod

class Bot(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def menu(self):
        pass

