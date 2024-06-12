from database.connection import conn, cursor

class Movies:

    all = {}

    def __init__(self, title, genre, release_date, rating, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.rating = rating

    @classmethod
    def create_table(cls):
        '''This is going to create a movies table in our db'''

        sql = '''
            CREATE TABLE IF NOT EXISTS movies(
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                release_date TIMESTAMP,
                rating INTEGER
            )
        '''
       
        cursor.execute(sql)
      
        conn.commit()


    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS movies;
        '''
        
        cursor.execute(sql)
      
        conn.commit()


    def save(self):
        sql = '''
            INSERT INTO movies (
                title,
                genre,
                release_date,
                rating
            ) VALUES (? ,? ,? ,?);
        '''
        cursor.execute(sql,(self.title, self.genre, self.release_date, self.rating),)

        conn.commit()

        self.id = cursor.lastrowid

        # update all the dict in the saved instance
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, genre, release_date, rating):
        movies = cls(title, genre, release_date, rating) 

        #  saving the instances in the db
        movies.save()

        return movies 

    
    def update(self):
        '''This updates an existing movie record in the database.'''
        sql = '''
            UPDATE movies SET title = ?, genre = ?, release_date = ?, rating = ? WHERE id = ?
        '''
        cursor.execute(sql, (self.title, self.genre, self.release_date, self.rating, self.id))
        conn.commit()


    def delete(self):
        sql = '''
            DELETE FROM movies WHERE id = ?;

        '''
        cursor.execute(sql, (self.id,))
        conn.commit()
    
    def __repr__(self):
        return f"< Movies{self.title} {self.genre} {self.release_date} {self.rating} >"

# mapping a database row to an object
    @classmethod
    def instance_from_db(cls, row):
        movies = cls.all.get(row[0])
        
        if movies:
            movies.title = row[1]
            movies.genre = row[2]
            movies.release_date = row[3]
            movies.rating = row[4]
        else:
            movies = cls(row[1], row[2], row[3], row[4])
            movies.id = row[0]

            cls.all[movies.id] = movies

        return movies


    @classmethod
    def fetch_all(cls):
        sql = 'SELECT * FROM movies;'
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows]