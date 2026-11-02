from Product import Product
from CanBeShipped import CanBeShipped

class physicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight
        
    def get_fulfilment_info(self):
        return f"Product requires physical shipping"  
    
    def calculate_shipping_cost(self):
        base_fee = 5.00
        cost_per_kg = 2.00
        return base_fee + (self.weight * cost_per_kg)
        
    def to_dict(self):
        return {
            "type": "physical",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "weight": self.weight
        }    
        
    def display_information(self):
        product_info = super().display_information()
        return  f"{product_info} | weight: {self.weight}"