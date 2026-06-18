from repositories.property import PropertyRepository
from utils import Print
from database import DB
from models.model import IModel
from decorators.error import logs

class Main:
    def __init__(self):
        self.__current_objects: list[IModel] = []
        self.__prop_repo: PropertyRepository = PropertyRepository()
        
    def __enter__(self):
        self.main_loop()
        
    def main_loop(self):
        self.__print_start_program()

        inp = self.__choice_want_to_do()
        
        while inp != "exit":
            match inp:
                # Dashboard
                case "1":
                    pass
                # GET
                case "2":
                    table = self.__choice_tables()
                    table = table.lower()
                    while table != "exit" or table != "back":
                        match(table):
                            # Property
                            case "1":
                                type = self.__choice_tables_type_search()
                                while type != "exit" or type != "back":
                                    match type:
                                        # All
                                        case "1":
                                            Print.values(self.__prop_repo.get_properties())
                                        # By id
                                        case "2":
                                            id = self.__choice_id()
                                            Print.value(self.__prop_repo.get_property_by_id(id))
                                    type = self.__choice_tables_type_search()
                                if type == "exit":
                                    table = "exit"
                        table = self.__choice_tables()  
                    if table == "exit":
                        break
                # POST
                case "3":
                    pass
                # PUT
                case "4":
                    pass
                # DELETE
                case "5":
                    pass
            inp = self.__choice_want_to_do()
        
    def __print_start_program(self):
        print("--------------------------------------")
        print("Starting program : Real Estate Manager")
        print("--------------------------------------\n")
        
    def __choice_want_to_do(self) -> str:
        print("What do you want to do ?")
        print("""1: NW - See dashboard\n
                2: Read data in tables\n
                3: NW - Add data in tables\n
                4: NW - Modify data in tables\n
                5: NW - Delete data from tables\n
                exit: Shutdown the program\n""")
        return input()
    
    def __choice_tables(self) -> str:
        print("""Which table do you want to see ?\n
                1: property\n
                back: Go back to previous menu\n
                exit: Shutdown the program\n""")
        return input()

    @logs
    def __choice_id(self) -> int:
        digit = input("""What id do you searching for ?\n""")
        while not digit.isdigit():
            digit = input("""What id do you searching for ?\n""")
        return int(digit)
    
    def __choice_tables_type_search(self) -> str:
        print("""What do your search ?\n
                1: All rows\n
                2: Specific id\n
                back: Go back to previous menu\n
                exit: Shutdown the program\n""")
        return input()
    
    def __exit__(self, exc_type, exc, tb):
        print("""------------------------------\n
                End of the Real Estate Manager\n
                ------------------------------""")
        

if __name__ == "__main__":
    db = DB()
    prop_rep = PropertyRepository()
    Main()
    if prop_rep is not None:
        # get all properties
        Print.values(prop_rep.get_properties())
        # get property with id 3
        Print.value(prop_rep.get_property_by_id(3))
        
        # Check value
        prop_rep.get_property_by_id(-1)
    
    db.close()