"""
Basic example of a trading bot with a strategy pattern. 
"""
import statistics
from abc import ABC, abstractmethod
from dataclasses import dataclass

from exchange import Exchange

class TradingStrategy(ABC):
    """Trading strategy that decides whether to buy or sell, given a list of prices."""

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool:
        """whether you should buy this coin, given the prices."""
    
    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool:
        """Whether you should sell this coin, given the prices."""