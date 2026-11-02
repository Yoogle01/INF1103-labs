from abc import abstractmethod,  ABC

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass