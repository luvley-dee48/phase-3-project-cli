from database.connection import conn, cursor

class Users:
    all = {}

    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

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

    @classmethod
    def drop_table(cls):
        '''Drop the users table if it exists'''
        sql_users = '''
            DROP TABLE IF EXISTS users;
        '''
        cursor.execute(sql_users)
        conn.commit()

    def save(self):
        '''Save the user instance to the database'''
        sql_users = '''
            INSERT INTO users (username, email, password) VALUES (?, ?, ?);
        '''
        cursor.execute(sql_users, (self.username, self.email, self.password))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, username, email, password):
        '''Create a new user instance and save it to the database'''
        user = cls(username, email, password)
        user.save()
        return user

    def update(self):
        '''Update the user instance in the database'''
        sql_users = '''
            UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?
        '''
        cursor.execute(sql_users, (self.username, self.email, self.password, self.id))
        conn.commit()

    def delete(self):
        '''Delete the user instance from the database'''
        sql_users = '''
            DELETE FROM users WHERE id = ?;
        '''
        cursor.execute(sql_users, (self.id,))
        conn.commit()

    def __repr__(self):
        return f"<Users {self.username} {self.email} {self.password}>"

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
