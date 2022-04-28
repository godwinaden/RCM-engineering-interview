class Customer:
    def __init__(self, customer_id: int,
                 customer_name: str,
                 contact_name: str,
                 address: str,
                 city: str,
                 country: str,
                 postal_code: int):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country