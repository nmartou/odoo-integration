from routes.test import TestQuery
from utils import Print
from database import DB

if __name__ == "__main__":
    db = DB()
    test = TestQuery.get_properties()
    if test is not None:
        Print.values(test)
    
    db.close()