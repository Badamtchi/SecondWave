"""
Basic example of a Trading bot with a strategy pattern.
"""
import statistics
from abc import ABC, abstractmethod
from dataclasses import dataclass

from exchange import Exchange

@dataclass
class StrategyParameters:
    """Class representing the union of possible parameters for the different strategies."""

    window_size: int = 3
    min_price: float = 32000.0
    max_price: float = 33000.0

class TradingStrategy(ABC):
    """Trading strategy that decides whether to buy or sell, given a list of prices"""

    @abstractmethod
    def should_buy(self, prices: list[float], params: StrategyParameters) -> bool:
        """Whether you should buy this coin, given the prices."""

    @abstractmethod
    def should_sell(self, prices: list[float], params: StrategyParameters) -> bool:
        """Whether you should sell this coin, given the prices."""

class AverageTradingStrategy(TradingStrategy):
    """Trading strategy based on price averages."""

    def should_buy(self, prices: list[float], params: StrategyParameters) -> bool:
        list_window = prices[-params.window_size :]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[float], params: StrategyParameters) -> bool:
        list_window = prices[-params.window_size :]
        return prices[-1] > statistics.mean(list_window)

