from abc import abstractmethod, ABC
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str ,price: float, stock: int, supplier: Supplier ):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier
        
    #get methods
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
            
    def get_stock(self):
        return self.__stock 
        
    #update stock        
    def update_stock(self, new_stock):
        self.__stock = new_stock
    
    @abstractmethod    
    def to_dict(self):
        pass  
        
    @abstractmethod
    def get_fulfilment_info(self):
        pass
        
    def display_information(self):
        return  f"Product_id: {self.__product_id} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}"
            
    def __str__ (self):
        return self.display_information()