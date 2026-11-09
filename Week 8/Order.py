from OrderLine import orderLine
from Product import Product
class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.order_lines: list[orderLine] = []
        
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = orderLine(product, quantity)
        self.order_lines.append(order_line)    
        
    def calculate_total(self) -> float:
        for line in self.order_lines:
            total = sum(line.calculate_subtotal())
            return total