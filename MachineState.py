from abc import ABC,abstractmethod

class State(ABC):

    @abstractmethod
    def in_state(self):
        pass

class HappyState(State):

    def in_state(self):
        print("I am in HAPPY state!")

class SadState(State):

    def in_state(self):
        print("I am in Sad state!")