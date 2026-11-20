from Supplier import Supplier
from Product import Product
from physicalProduct import physicalProduct
from digitalProduct import digitalProduct

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, weight: int, download_size: int, supplier: Supplier) -> Product:
        
        if product_type == "physical":
            return physicalProduct(product_id, name, price, stock_quantity, weight, supplier)
        elif product_type == "digital" :
            return digitalProduct(product_id, name, price, stock_quantity, download_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")