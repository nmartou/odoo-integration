from dataclasses import dataclass

@dataclass
class Property:
    id_property: int
    price: float
    property_type: str
    address_id: int
    
    def update_price(self, new_price):
        self.price = new_price