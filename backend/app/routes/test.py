from decorators.db_decorators import with_cursor
from models.property import Property

class TestQuery:
    @staticmethod
    @with_cursor(model=Property)
    def get_properties(db = None) -> list[Property]:
        query = "SELECT * FROM property;"
        if db is None:
            raise ValueError("[Error] get_properties is empty :", db)
        db.execute(query)
        return db.fetchall()