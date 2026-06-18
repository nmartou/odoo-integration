from functools import wraps

def logs(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        try:
            func(*arg, **kwargs)
        except ValueError as e:
            print(e)
        
    return wrapper