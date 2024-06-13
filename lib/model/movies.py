from database.connection import conn, cursor

class Movies:
# will define the class to represent a movie record 
    all = {}
# the all in this case will act as the dictonary to store the movie objects by their IDS
    def __init__(self, title, genre, release_date, rating, id=None):
        # the constractor for my movies class
        self.id = id
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.rating = rating

    @classmethod
    # this is a method that will create the movies table if it doesn't already exist
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
    # this is a class method that will drop the movies table if it already exists
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS movies;
        '''
        
        cursor.execute(sql)
      
        conn.commit()


    # this is a method that will save the movies object to the database. It can also update the all dictonary within the saved object
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

    # creates a new movies object and calls the save method in order to return the created movie object
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