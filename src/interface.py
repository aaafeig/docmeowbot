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
    def ask_request(self, message):
        pass

    @abstractmethod
    def manage(self):
        pass
