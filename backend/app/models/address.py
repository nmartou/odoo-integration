from dataclasses import dataclass

@dataclass
class Address:
    id_address: int = None
    street: str = ""
    appartment_number: str = ""
    postcode: int = None
    city: str = ""
    country: str = ""