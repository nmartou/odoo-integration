import os
from dotenv import load_dotenv
import psycopg

class DB:
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def connect(self):
        load_dotenv()
        
        USER = os.getenv("USER")
        PASSWORD = os.getenv("PASSWORD")
        HOST = os.getenv("HOST")
        PORT = os.getenv("PORT")
        DB_NAME = os.getenv("DB_NAME")

        if USER is None or PASSWORD is None or HOST is None or PORT is None or DB_NAME is None:
            raise ValueError("[Error] database url is incorrect :", USER, PASSWORD, HOST, PORT, DB_NAME)
    
        return self.get_connection(USER, PASSWORD, HOST, PORT, DB_NAME)
    
    def get_connection(self, user:str, password:str, host:str, port:str, db_name:str):
        if self._instance and (self._connection is None or self._connection.closed):
            self._connection = psycopg.connect(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
        return self._connection
    
    def close(self):
        if self._instance and (self._connection is not None and not self._connection.closed):
            self._connection.close()
            self._connection = None