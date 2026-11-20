from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
    
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):
    def apply(self, total) -> float:
        total = total * 0.9
        return total
    
class BulkPercentage(DiscountStrategy):
    def apply(self, total:float) -> float:
        return total - 20 if total >= 200 else total
    
class StudentDiscount(DiscountStrategy):
    def apply(self, total:  float) -> float:
        return total * 0.10
    
    