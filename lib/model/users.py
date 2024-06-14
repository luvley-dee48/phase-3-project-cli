from database.connection import conn, cursor

class Users:
    # all acts as a dictonary to store user objects 
    all = {}
    # the init will became a constructor for the users class
    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    # the property is used to define the getter and setter methods
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        # Add any constraints or validation you need
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Add any constraints or validation you need
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        # Add any constraints or validation you need
        self._password = value

    # This method creates the "users" table in the database if it doesn't exist.
    @classmethod
    def create_table(cls):
        '''Create the users table in the database'''
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

    # this will drop the users table 
    @classmethod
    def drop_table(cls):
        '''Drop the users table if it exists'''
        sql_users = '''
            DROP TABLE IF EXISTS users;
        '''
        cursor.execute(sql_users)
        conn.commit()

    # This method saves the user object to the database. Will also updates the object's id with the newly generated ID and adds the object to the all dictionary.
    def save(self):
        '''Save the user instance to the database'''
        sql_users = '''
            INSERT INTO users (username, email, password) VALUES (?, ?, ?);
        '''
        cursor.execute(sql_users, (self.username, self.email, self.password))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    # creating new user objects
    @classmethod
    def create(cls, username, email, password):
        '''Create a new user instance and save it to the database'''
        user = cls(username, email, password)
        user.save()
        return user

    # This method updates an existing user record in the database based on the object.
    def update(self):
        '''Update the user instance in the database'''
        sql_users = '''
            UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?
        '''
        cursor.execute(sql_users, (self.username, self.email, self.password, self.id))
        conn.commit()

    # This method deletes the user record associated with the object from the database
    def delete(self):
        '''Delete the user instance from the database'''
        sql_users = '''
            DELETE FROM users WHERE id = ?;
        '''
        cursor.execute(sql_users, (self.id,))
        conn.commit()

    #  shows how the the object is represented as a strin
    def __repr__(self):
        return f"<Users {self.username} {self.email} {self.password}>"
    
    # This class method takes a database row (tuple) and tries to find a corresponding user object in the all dictionary using the ID. 

    @classmethod
    def instance_from_db(cls, row):
        '''Create a user instance from a database row'''
        user = cls.all.get(row[0])
        if user:
            user.username = row[1]
            user.email = row[2]
            user.password = row[3]
        else:
            user = cls(row[1], row[2], row[3])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def fetch_all(cls):
        '''Fetch all users from the database'''
        sql_users = 'SELECT * FROM users;'
        cursor.execute(sql_users)
        rows = cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows]


    