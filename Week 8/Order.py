from OrderLine import orderLine
from Product import Product
from discountStrategy import DiscountStrategy

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.order_lines: list[orderLine] = []
        self.discount = DiscountStrategy
        
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = orderLine(product, quantity)
        self.order_lines.append(order_line)    
        
    def calculate_total(self) -> float:
        total =  sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

    def set_discount():
        pass