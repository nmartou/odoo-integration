from models.property import Property
from decorators.db_decorators import with_cursor
from utils import Print
from repositories.repository import IRepository
from models.model import IModel
from typing import Sequence

class PropertyRepository(IRepository):
    @with_cursor(model=Property)
    def get_properties(self, db = None) -> Sequence[Property]:
        query = "SELECT * FROM property;"
        if db is None:
            raise ValueError("[Error] get_properties connection is empty :", db)
        db.execute(query)
        return db.fetchall()
    
    @with_cursor(model=Property)
    def get_property_by_id(self, id : int, db = None) -> Property:
        query = "SELECT * FROM property WHERE id_property = %s"
        if db is None:
            raise ValueError("[Error] get_properties connection is empty :", db)
        if id == -1:
            raise ValueError("[Error] id is not specified :", id)
        
        db.execute(query, [id])
        return db.fetchone()