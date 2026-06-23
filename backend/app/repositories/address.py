from repositories.repository import IRepository
from models.address import Address
from decorators.error import logs
from decorators.db_decorators import with_cursor
from psycopg.errors import ForeignKeyViolation
from typing import Sequence

class AddressRepository(IRepository):
    @logs
    @with_cursor(model=Address)
    def get_all(self, db = None) -> Sequence[Address]:
        query = "SELECT * FROM address;"
        
        if db is None:
            raise ValueError("[Error] get_all - connection is empty :", db)
        
        try:
            db.execute(query)
            return db.fetchall()
        except Exception as e:
            print(f"[Error] get_all - Error occurred while fetching addresses: {e}")
            raise
    
    @logs
    @with_cursor(model=Address)
    def get_by_id(self, id: int, db = None) -> Address:
        query = "SELECT * FROM address WHERE id_address = %s"
        if db is None:
            raise ValueError("[Error] get_by_id - connection is empty :", db)
        if id < 1:
            raise ValueError(f"[Error] get_by_id - id is not correct : {id}")
        
        try:
            db.execute(query, [id])
            return db.fetchone()
        except Exception as e:
            print(f"[Error] get_by_id - Error occurred while fetching address: {e}")
            raise
    
    @logs
    @with_cursor(model=Address)
    def modify_by_id(self, object: Address, db = None) -> Address:
        if not object.check_values():
            raise ValueError(f"[Error] modify_by_id - Invalid address values")
        query = "UPDATE address SET street = %s, appartment_number = %s, city = %s, country = %s, postcode = %s WHERE id_address = %s RETURNING *;"
        if db is None:
            raise ValueError("[Error] modify_by_id - connection is empty :", db)
        
        try:             
            db.execute(query, (object.street, object.appartment_number, object.city, object.country, object.postcode, object.id_address))
            return db.fetchone()
        except Exception as e:
            print(f"[Error] modify_by_id - Error occurred while modifying address: {e}")
            raise
        
    
    @logs
    @with_cursor(model=Address)
    def add(self, object: Address, db = None) -> Address:
        if not object.check_values():
            raise ValueError(f"[Error] add_address - Invalid address values")
        
        query = "INSERT INTO address (street, appartment_number, city, country, postcode) VALUES (%s, %s, %s, %s, %s) RETURNING *;"
        
        if db is None:
            raise ValueError("[Error] add_address - connection is empty :", db)
        try:
            db.execute(query, (object.street, object.appartment_number, object.city, object.country, object.postcode))
            return db.fetchone()
        except Exception as e:
            print(f"[Error] add_address - Error occurred while adding address: {e}")
            raise
    
    @logs
    @with_cursor(model=Address)
    def delete_by_id(self, id: int, db = None):
        query = "DELETE FROM address WHERE id_address = %s;"
        if db is None:
            raise ValueError("[Error] delete_by_id - connection is empty :", db)
        if type(id) != int:
            raise TypeError(f"[Error] delete_by_id - id is not an integer : {id}")
        elif id < 1:
            raise ValueError(f"[Error] delete_by_id - id is not correct : {id}")
        
        try:
            db.execute(query, [id])
            return
        except Exception as e:
            print(f"[Error] delete_by_id - Error occurred while deleting address: {e}")
            raise
        
    @logs
    def get_model_type(self) -> type[Address]:
        return Address