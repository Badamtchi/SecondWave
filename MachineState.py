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



class Event(ABC):

    @abstractmethod
    def in_event(self):
        pass

class LostMoney(Event):

    def in_event(self):
        print("I lost money((")

class RecvMoney(Event):

    def in_event(self):
        print("I got money))")


class StateMachine():

    def __init__(self):
        self.currstate = HappyState()

    def current_state(self):
        print(self.currstate.in_state())
    
    def recv_event(self, event):
        if isinstance(event, LostMoney):
            self.currstate = SadState()
        else:
            self.currstate = HappyState()


sm = StateMachine()
sm.current_state()
sm.recv_event(LostMoney())
sm.current_state()
sm.recv_event(RecvMoney())
sm.current_state()