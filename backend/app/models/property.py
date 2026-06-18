from dataclasses import dataclass
from models.model import IModel

@dataclass
class Property(IModel):
    id_property: int
    price: float
    property_type: str
    address_id: int
    
    def update_price(self, new_price):
        self.price = new_price