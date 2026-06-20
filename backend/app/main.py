from decimal import Decimal

from data_types.property import PropertyType
from models.property import Property
from repositories.property import PropertyRepository
from utils import Converter, Print
from database import DB
from models.model import IModel
from decorators.error import logs
import os

class Main:
    def __init__(self):
        self.__current_objects: list[IModel] = []
        self.__prop_repo: PropertyRepository = PropertyRepository()
        
    def __enter__(self):
        self.main_loop()
        
    @logs
    def main_loop(self):
        self.__clear_console()
        self.__print_start_program()

        inp = self.__choice_want_to_do()
        self.__clear_console()
        
        while inp != "exit":
            match inp:
                # Dashboard
                case "1":
                    pass
                # GET
                case "2":
                    table = self.__choice_tables()
                    self.__clear_console()
                    table = table.lower()
                    while table != "exit" and table != "b":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_get()
                                self.__clear_console()
                                while type != "exit" and type != "b":
                                    match type:
                                        # All
                                        case "1":
                                            Print.values(self.__prop_repo.get_all())
                                            self.__print_waiting()
                                            self.__clear_console()
                                        # By id
                                        case "2":
                                            id = self.__choice_id()
                                            Print.value(self.__prop_repo.get_all(id))
                                            self.__print_waiting()
                                            self.__clear_console()
                                    type = self.__choice_tables_type_search_get()
                                    self.__clear_console()
                                if type == "exit":
                                    table = "exit"
                        if table == "exit":
                            break
                        table = self.__choice_tables()
                        self.__clear_console()
                    if table == "exit":
                        break
                # POST
                case "3":
                    table = self.__choice_tables()
                    self.__clear_console()
                    table = table.lower()
                    while table != "exit" and table != "b":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_post()
                                self.__clear_console()
                                while type != "exit" and type != "b":
                                    match type:
                                        # Add new property
                                        case "1":
                                            Print.values(self.__prop_repo.add(self.__choice_add(Property)))
                                            self.__print_waiting()
                                            self.__clear_console()
                                    type = self.__choice_tables_type_search_post()
                                    self.__clear_console()
                                if type == "exit":
                                    table = "exit"
                        if table == "exit":
                            break
                        table = self.__choice_tables()
                        self.__clear_console()
                    if table == "exit":
                        break
                # PUT
                case "4":
                    table = self.__choice_tables()
                    self.__clear_console()
                    table = table.lower()
                    while table != "exit" and table != "b":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_put()
                                self.__clear_console()
                                while type != "exit" and type != "b":
                                    match type:
                                        # Modify property by id
                                        case "1":
                                            id = self.__choice_id()
                                            self.__clear_console()
                                            
                                            property = self.__prop_repo.get_by_id(id)
                                            Print.value(property)
                                            
                                            property.price = Converter.money_to_decimal(property.price)
                                            property = self.__choice_update(property)
                                            self.__clear_console()
                                            
                                            Print.value(self.__prop_repo.modify_by_id(property))
                                            self.__print_waiting()
                                            self.__clear_console()
                                    type = self.__choice_tables_type_search_put()
                                    self.__clear_console()
                                if type == "exit":
                                    table = "exit"
                        if table == "exit":
                            break
                        table = self.__choice_tables()
                        self.__clear_console()
                    if table == "exit":
                        break
                # DELETE
                case "5":
                    table = self.__choice_tables()
                    self.__clear_console()
                    table = table.lower()
                    while table != "exit" and table != "b":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_delete()
                                self.__clear_console()
                                while type != "exit" and type != "b":
                                    match type:
                                        # Delete property by id
                                        case "1":
                                            id = self.__choice_id()
                                            self.__clear_console()
                                            
                                            property = self.__prop_repo.get_by_id(id)
                                            Print.value(property)
                                            
                                            if self.__confirm(f"Are you sure you want to delete the property with id {property.id_property} ?"):
                                                self.__clear_console()
                                            
                                                Print.value(self.__prop_repo.delete_by_id(property.id_property))
                                                print("[Info] Property deleted successfully")
                                                self.__print_waiting()
                                                self.__clear_console()
                                    self.__clear_console()
                                    type = self.__choice_tables_type_search_delete()
                                    self.__clear_console()
                                if type == "exit":
                                    table = "exit"
                        if table == "exit":
                            break
                        table = self.__choice_tables()
                        self.__clear_console()
                    if table == "exit":
                        break
            inp = self.__choice_want_to_do()
            self.__clear_console()
        self.__print_end_program()
        
    def __print_start_program(self):
        print("--------------------------------------")
        print("Starting program : Real Estate Manager")
        print("--------------------------------------\n")
        
    def __choice_want_to_do(self) -> str:
        print("What do you want to do ?")
        print("""1: NW - See dashboard\n2: Read data in tables\n3: Add data in tables\n4: Modify data in tables\n5: Delete data from tables\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables(self) -> str:
        print("""Which table do you want ?\n1: property\nb: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __print_waiting(self):
        input("--- ENTER to continue ---\n")

    @logs
    def __choice_id(self) -> int:
        digit = input("""Which id do you searching for ?\n""")
        while not digit.isdigit():
            digit = input("""Which id are you searching for ?\n""")
        return int(digit)

    @logs
    def __choice_add(self, object_type: IModel) -> IModel:
        obj = object_type()
        keys = obj.__dict__.keys()
        keys = list(keys)
        keys.pop(0)
        for key in keys:
            value = input(f"Enter {key} :")
            type_value = type(getattr(obj, key))
            if type_value == int:
                value = int(value)
            elif type_value == float:
                value = float(value)
            elif type_value == Decimal:
                value = Decimal(value)
            elif type_value == PropertyType:
                if PropertyType[value] is None:
                    print(f"[Error] Invalid value for {key} : {value}")
                    continue
                
            setattr(obj, key, value)
            
        return obj
    
    @logs
    def __choice_update(self, obj: IModel) -> IModel:
        keys = obj.__dict__.keys()
        keys = list(keys)
        keys.pop(0)
        for key in keys:
            value = input(f"Would like to update (n (no) or <new_value>) {key} :")
            if value == "n":
                continue
            type_value = type(getattr(obj, key))
            if type_value == int:
                value = int(value)
            elif type_value == float:
                value = float(value)
            elif type_value == Decimal:
                value = Decimal(value)
            elif type_value == PropertyType:
                if PropertyType[value] is None:
                    print(f"[Error] Invalid value for {key} : {value}")
                    continue
                
            setattr(obj, key, value)
            
        return obj

    def __choice_tables_type_search_get(self) -> str:
        print("""What do you want to search ?\n1: All rows\n2: Specific id\nb: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables_type_search_post(self) -> str:
        print("""What do you want to do ?\n1: Add new row\nb: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables_type_search_put(self) -> str:
        print("""What do you want to do ?\n1: Modify row\nb: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables_type_search_delete(self) -> str:
        print("""What do you want to do ?\n1: Delete row\nb: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __print_end_program(self):
        print("""----------------------------------------\nEnd of the program : Real Estate Manager\n----------------------------------------""")
        
    def __confirm(self, message: str) -> bool:
        print(f"{message} (y/n)")
        choice = input()
        while choice not in ["y", "n"]:
            print(f"{message} (y/n)")
            choice = input()
        return choice == "y"
        
    def __clear_console(self):
        os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    db = DB()
    # prop_rep = PropertyRepository()
    
    # Test the repositories
    # if prop_rep is not None:
        # get all properties
        # Print.values(prop_rep.get_properties())
        # get property with id 3
        # Print.value(prop_rep.get_property_by_id(3))
        
        # Check value
        # prop_rep.get_property_by_id(-1)

    Main().main_loop()
    
    db.close()