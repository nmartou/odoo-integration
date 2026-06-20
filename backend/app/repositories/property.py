from models.property import Property
from decorators.db_decorators import with_cursor
from repositories.repository import IRepository
from typing import Sequence
from decorators.error import logs
from data_types.property import PropertyType
from decimal import Decimal
from utils import Converter

class PropertyRepository(IRepository):
    @logs
    @with_cursor(model=Property)
    def get_all(self, db = None) -> Sequence[Property]:
        query = "SELECT * FROM property;"
        
        if db is None:
            raise ValueError("[Error] get_properties - connection is empty :", db)
        
        db.execute(query)
        
        return db.fetchall()
    
    @logs
    @with_cursor(model=Property)
    def get_by_id(self, id : int, db = None) -> Property:
        query = "SELECT * FROM property WHERE id_property = %s"
        if db is None:
            raise ValueError("[Error] get_property_by_id - connection is empty :", db)
        if id < 1:
            raise ValueError(f"[Error] get_property_by_id - id is not correct : {id}")
        
        db.execute(query, [id])
        return db.fetchone()
    
    @logs
    @with_cursor(model=Property)
    def add(self, property: Property, db = None) -> Property:
        if not property.check_values():
            raise ValueError(f"[Error] add_property - Invalid property values")
        
        query = "INSERT INTO property (price, property_type, address_id) VALUES (%s, %s, %s) RETURNING *;"
        
        if db is None:
            raise ValueError("[Error] add_property - connection is empty :", db)
        db.execute(query, (property.price, property.property_type, property.address_id))
        return db.fetchone()
    
    @logs
    @with_cursor(model=Property)
    def modify_by_id(self, property: Property, db = None) -> Property:
        """Modify the property with a specific id

        Args:
            property (Property): The property object with updated values
            db (_type_, optional): object to use to manage the database. Defaults to None.
        """
        if not property.check_values():
            raise ValueError(f"[Error] modify_by_id - Invalid property values")
        query = "UPDATE property SET price = %s, property_type = %s, address_id = %s WHERE id_property = %s RETURNING *;"
        if db is None:
            raise ValueError("[Error] modify_by_id - connection is empty :", db)
        
        db.execute(query, (property.price, property.property_type, property.address_id, property.id_property))
        return db.fetchone()
    
    @logs
    @with_cursor(model=Property)
    def delete_by_id(self, id: int, db = None):
        query = "DELETE FROM property WHERE id_property = %s;"
        if db is None:
            raise ValueError("[Error] delete_by_id - connection is empty :", db)
        if id < 1:
            raise ValueError(f"[Error] delete_by_id - id is not correct : {id}")
        
        db.execute(query, [id])