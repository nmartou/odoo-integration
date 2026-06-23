from abc import ABC, abstractmethod
from models.model import IModel
from typing import Sequence, Generic, TypeVar

T = TypeVar("T", bound=IModel)

class IRepository(Generic[T], ABC):
    @abstractmethod
    def get_by_id(self, id) -> T:
        pass
    
    @abstractmethod
    def get_all(self) -> Sequence[T]:
        pass
    
    @abstractmethod
    def modify_by_id(self, object: T) -> T:
        pass
    
    @abstractmethod
    def add(self, object: T) -> T:
        pass
    
    @abstractmethod
    def get_model_type(self) -> type[T]:
        pass