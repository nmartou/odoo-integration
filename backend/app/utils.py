from models.model import IModel
from typing import Sequence
from tabulate import tabulate
from decorators.error import logs
from decimal import Decimal

class Print:
    @staticmethod
    @logs
    def values(objs: Sequence[IModel]):
        if objs is None:
            raise ValueError("[Error] values - objects is empty")
        if len(objs) < 1:
            raise ValueError("[Error] values - No objects finded :", objs)
        keys = objs[0].__dict__.keys()
        keys = [str(n) for n in keys]
        values = []
        for property in objs:
            values.append([property.__getattribute__(n) for n in keys])
            
        print(tabulate(values, headers=keys))
    
    @staticmethod
    @logs
    def value(obj: IModel):
        if obj is None:
            raise ValueError("[Error] value - object is empty")
        keys = obj.__dict__.keys()
        keys = [str(n) for n in keys]
        value = [[obj.__getattribute__(n) for n in keys]]
        print(tabulate(value, headers=keys))
        
class Converter:
    @staticmethod
    @logs
    def money_to_decimal(string: str) -> Decimal:
        string = string.replace(",", "").replace("€", "").strip()
        return Decimal(string)