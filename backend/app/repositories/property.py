from models.property import Property
from decorators.db_decorators import with_cursor
from repositories.repository import IRepository
from typing import Sequence
from decorators.error import logs
from data_types.property import PropertyType

class PropertyRepository(IRepository):
    @logs
    @with_cursor(model=Property)
    def get_properties(self, db = None) -> Sequence[Property]:
        query = "SELECT * FROM property;"
        
        if db is None:
            raise ValueError("[Error] get_properties - connection is empty :", db)
        
        db.execute(query)
        
        return db.fetchall()
    
    @logs
    @with_cursor(model=Property)
    def get_property_by_id(self, id : int, db = None) -> Property:
        query = "SELECT * FROM property WHERE id_property = %s"
        if db is None:
            raise ValueError("[Error] get_property_by_id - connection is empty :", db)
        if id < 1:
            raise ValueError(f"[Error] get_property_by_id - id is not correct : {id}")
        
        db.execute(query, [id])
        return db.fetchone()
    
    @logs
    @with_cursor(model=Property)
    def add_property(self, property: Property, db = None) -> Property:
        if not property.check_values():
            raise ValueError(f"[Error] add_property - Invalid property values")
        
        query = "INSERT INTO property (price, property_type, address_id) VALUES (%s, %s, %s) RETURNING *;"
        
        if db is None:
            raise ValueError("[Error] get_properties - connection is empty :", db)
        db.execute(query, (property.price, property.property_type, property.address_id))
        return db.fetchone()
    
    @logs
    @with_cursor(model=Property)
    def modify_by_id(self, id: int, price: float, property_type: PropertyType, address_id: int | None = None, db = None) -> Property:
        """Modify the property with a specific id

        Args:
            id (int): id of the id_property
            price (float): price of the property
            property_type (PropertyType): property_type defined in a specific range of values
            address_id (int | None, optional): physical address of the property. Defaults to None.
            db (_type_, optional): object to use to manage the database. Defaults to None.
        """
        if price < 0:
            raise ValueError(f"[Error] get_properties - price is lower than zero : {price}")
        query = "UPDATE property (price, property_type, address_id) RETURNING *;"
        if db is None:
            raise ValueError("[Error] get_properties - connection is empty :", db)
        
        db.execute(query, (price, property_type, address_id))
        return db.fetchone()