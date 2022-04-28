class Product:

    def __init__(self,
                 product_id: int,
                 product_name: str,
                 supplier_id: int,
                 category_id: int,
                 unit: str,
                 price: float):
        self.product_id = product_id
        self.product_name = product_name
        self.supplier_id = supplier_id
        self.category_id = category_id
        self.unit = unit
        self.price = price
