from dataclasses import dataclass

@dataclass
class Address:
    id_address: int = None
    street: str = ""
    appartment_number: str = None
    postcode: int = None
    city: str = ""
    country: str = ""
    
    def check_values(self):
        if type(self.id_address) != int and self.id_address is not None:
            print(f"[Error] Address model - id_address is not an integer or null value : {type(self.id_address)} {self.id_address}")
            return False
        elif type(self.id_address) == int and self.id_address < 1:
            print(f"[Error] Address model - id_address is lower than 1 : {self.id_address}")
            return False
        if type(self.street) != str:
            print(f"[Error] Address model - street is not a string : {type(self.street)} {self.street}")
            return False
        if type(self.appartment_number) != str and self.appartment_number is not None:
            print(f"[Error] Address model - appartment_number is not a string or null value : {type(self.appartment_number)} {self.appartment_number}")
            return False
        if type(self.postcode) != int or self.postcode is None:
            print(f"[Error] Address model - postcode is not an integer or is null : {type(self.postcode)} {self.postcode}")
            return False
        if type(self.city) != str:
            print(f"[Error] Address model - city is not a string : {type(self.city)} {self.city}")
            return False
        if type(self.country) != str:
            print(f"[Error] Address model - country is not a string : {type(self.country)} {self.country}")
            return False
        return True