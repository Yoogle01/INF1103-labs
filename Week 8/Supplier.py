class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
        
    def display_information(self):
        return f"Supplier id:{self.supplier_id} | Name: {self.name} | Contact email address: {self.contact_email}"