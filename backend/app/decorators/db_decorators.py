from functools import wraps
from database import DB
from psycopg.rows import class_row
from decorators.error import logs

def with_cursor(model):
    def decorator(func):
        @logs
        @wraps(func)
        def wrapper(*args, **kwargs):
            conn = DB().connect()
            factory = class_row(model) if model else None
            
            if conn is None:
                raise ValueError("[Error] Factory is empty :", conn)
            if not factory:
                raise ValueError("[Error] Factory type is empty :", factory)
            
            with conn.cursor(row_factory=factory) as db:
                try:
                    result = func(*args, db, **kwargs)
                    conn.commit()
                    return result
                except Exception:
                    conn.rollback()
                    raise
        return wrapper
    return decorator