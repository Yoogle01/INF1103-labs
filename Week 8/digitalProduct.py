from Product import Product
from Supplier import Supplier

class digitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.download_size = download_size
    
    def get_fulfilment_info(self):
        return f"Product is delivered digitally"    
    
    def to_dict(self):
        return {
            "type": "digital",
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "download_size": self.download_size
        }
        
    def display_information(self):
        product_info = super().display_information()
        return  f"{product_info} | Download size: {self.download_size}"    