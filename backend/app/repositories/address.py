from repositories.repository import IRepository
from models.address import Address
from decorators.error import logs
from decorators.db_decorators import with_cursor

class AddressRepository(IRepository):
    @logs
    @with_cursor(model=Address)
    def get_all(self) -> list[Address]:
        pass
    
    @logs
    @with_cursor(model=Address)
    def get_by_id(self, id: int) -> Address:
        pass
    
    @logs
    @with_cursor(model=Address)
    def modify_by_id(self, address: Address) -> Address:
        pass
    
    @logs
    @with_cursor(model=Address)
    def add(self, address: Address) -> Address:
        pass
    
    @logs
    @with_cursor(model=Address)
    def delete_by_id(self, id: int) -> Address:
        pass