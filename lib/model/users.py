
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

    
    @classmethod
    def drop_table(cls):
        sql_users= '''
            DROP TABLE IF EXISTS users;
        '''
        
        cursor.execute(sql_users)
      
        conn.commit()


    def save(self):
        sql_users = '''
            INSERT INTO users (
                username,
                email,
                password,
                
            ) VALUES (? ,? ,?);
        '''
        cursor.execute(sql_users,(self.username, self.email, self.password),)

        conn.commit()

        self.id = cursor.lastrowid


    
    @classmethod
    def create(cls, username, email, password):
        users = cls(username, email, password) 

        #  saving the instances in the db
        users.save()

        return users
    
    
    def update(self):
        '''This updates an existing movie record in the database.'''
        sql_users = '''
            UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?
        '''
        cursor.execute(sql_users, (self.username, self.email, self.password, self.id))
        conn.commit()


    def delete(self):
        sql_users = '''
            DELETE FROM users WHERE id = ?;

        '''
        cursor.execute(sql_users, (self.id,))
        conn.commit()
    
    def __repr__(self):
        return f"< Users{self.username} {self.email} {self.password} >"

# mapping a database row to an object
    @classmethod
    def instance_from_db(cls, row):
        users = cls.all.get(row[0])
        
        if users:
            users.username = row[1]
            users.email = row[2]
            users.password = row[3]
          
        else:
            users = cls(row[1], row[2], row[3])
            users.id = row[0]

            cls.all[users.id] = users

        return users


    @classmethod
    def fetch_all(cls):
        sql_users = 'SELECT * FROM users;'
        cursor.execute(sql_users)
        rows = cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows]
