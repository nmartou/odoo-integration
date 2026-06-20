from abc import ABC, abstractmethod
from models.model import IModel

class IRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> IModel:
        pass
    
    @abstractmethod
    def get_all(self) -> list[IModel]:
        pass
    
    @abstractmethod
    def modify_by_id(self, object: IModel) -> IModel:
        pass
    
    @abstractmethod
    def add(self, object: IModel) -> IModel:
        pass