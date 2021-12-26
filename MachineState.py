from abc import ABC,abstractmethod

class State(ABC):

    @abstractmethod
    def in_state(self):
        pass

