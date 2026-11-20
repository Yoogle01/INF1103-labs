class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        if not supplier_id or not str(supplier_id).strip():
            raise ValueError("Supplier ID cannot be empty.")
        if not name or not str(name).strip():
            raise ValueError("Supplier name cannot be empty.")
        if not contact_email or "@" not in contact_email:
            raise ValueError("Contact email must be a valid email address.")
        
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
        
    def display_information(self):
        return f"Supplier id:{self.supplier_id} | Name: {self.name} | Contact email address: {self.contact_email}"