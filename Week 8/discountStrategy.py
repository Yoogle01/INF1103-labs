from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
    
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):
    def apply(self, percent: float) -> float:
        return percent
    
class BulkPercentage(DiscountStrategy):
    def apply(self, total:float, percent: float) -> float:
        threshold = total * percent
        return threshold
    
    