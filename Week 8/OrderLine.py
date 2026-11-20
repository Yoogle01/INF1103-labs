from Product import Product
class orderLine:
    def __init__(self, product: Product, quantity: int):
        if product is None:
            raise ValueError("Product cannot be None.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity
        
    def calculate_subtotal(self) -> float:
        return self.product.get_price * self.quantity  