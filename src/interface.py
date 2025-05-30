from abc import ABC, abstractmethod

class BotView(ABC):

    @abstractmethod
    def start(self, message):
        pass

    @abstractmethod
    def menu(self):
        pass

class BotLogic(ABC):

    @abstractmethod
    def add_doc(self, doc):
        pass

    @abstractmethod
    def search(self, request: str):
        pass

    @abstractmethod
    def manage(self):
        pass