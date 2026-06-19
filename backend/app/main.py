from decimal import Decimal

from data_types.property import PropertyType
from models.property import Property
from repositories.property import PropertyRepository
from utils import Print
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
                    while table != "exit" and table != "back":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_get()
                                self.__clear_console()
                                while type != "exit" and type != "back":
                                    match type:
                                        # All
                                        case "1":
                                            Print.values(self.__prop_repo.get_properties())
                                            self.__print_waiting()
                                            self.__clear_console()
                                        # By id
                                        case "2":
                                            id = self.__choice_id()
                                            Print.value(self.__prop_repo.get_property_by_id(id))
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
                    while table != "exit" and table != "back":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search_post()
                                self.__clear_console()
                                while type != "exit" and type != "back":
                                    match type:
                                        # Add new property
                                        case "1":
                                            Print.values(self.__prop_repo.add_property(self.__choice_add(Property)))
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
                    pass
                # DELETE
                case "5":
                    pass
            inp = self.__choice_want_to_do()
            self.__clear_console()
        self.__print_end_program()
        
    def __print_start_program(self):
        print("--------------------------------------")
        print("Starting program : Real Estate Manager")
        print("--------------------------------------\n")
        
    def __choice_want_to_do(self) -> str:
        print("What do you want to do ?")
        print("""1: NW - See dashboard\n2: Read data in tables\n3: NW - Add data in tables\n4: NW - Modify data in tables\n5: NW - Delete data from tables\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables(self) -> str:
        print("""Which table do you want to see ?\n1: property\nback: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __print_waiting(self):
        input("--- ENTER to continue ---\n")

    @logs
    def __choice_id(self) -> int:
        digit = input("""What id do you searching for ?\n""")
        while not digit.isdigit():
            digit = input("""What id do you searching for ?\n""")
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

    def __choice_tables_type_search_get(self) -> str:
        print("""What do you want to search ?\n1: All rows\n2: Specific id\nback: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __choice_tables_type_search_post(self) -> str:
        print("""What do you want to do ?\n1: Add new row\nback: Go back to previous menu\nexit: Shutdown the program\n""")
        return input()
    
    def __print_end_program(self):
        print("""----------------------------------------\nEnd of the program : Real Estate Manager\n----------------------------------------""")
        
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