
from database.connection import conn, cursor

class Users:
    def __init__(self,username,email,password,id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def create_table(cls):
        '''This is going to create a movies table in our db'''
        
    sql_users = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            password TEXT
        )
    '''

    cursor.execute(sql_users)
      
    conn.commit()