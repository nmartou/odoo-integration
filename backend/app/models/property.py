from dataclasses import dataclass
from decimal import Decimal
from decorators.error import logs
from models.model import IModel
from data_types.property import PropertyType

@dataclass
class Property(IModel):
    id_property: int = None
    price: Decimal = Decimal("0.0")
    property_type: str = "FIELD"
    address_id: int = None
    
    def update_price(self, new_price):
        self.price = new_price
    
    @logs
    def check_values(self):
        if type(self.price) != Decimal:
            print(f"[Error] Property model - price is not a Decimal : {type(self.price)} {self.price}")
            return False 
        elif self.price < 0:
            print(f"[Error] Property model - price is lower than zero : {self.price}")
            return False
        if PropertyType[self.property_type] is None:
            print(f"[Error] Property model - property_type is not correct : {self.property_type}")
            return False
        if self.address_id is not None:
            if self.address_id is "":
                self.address_id = None
                return True
            elif type(self.address_id) == int and self.address_id < 1:
                print(f"[Error] Property model - address_id is not correct : {self.address_id}")
                return False
        return True