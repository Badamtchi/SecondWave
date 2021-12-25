import string
import random
from typing import List
from abc import ABC, abstractmethod

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choice(string.ascii_uppercase, k=length))

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()

