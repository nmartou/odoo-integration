from repositories.property import PropertyRepository
from utils import Print
from database import DB

if __name__ == "__main__":
    db = DB()
    prop_rep = PropertyRepository()
    if prop_rep is not None:
        Print.values(prop_rep.get_properties())
    
    db.close()