from database.connection import conn, cursor
class Reviews:
    def __init__(self,movie_id,user_id,review_text,rating,id=None):
        self.id = id
        self.movie_id = movie_id
        self.user_id = user_id
        self.review_text = review_text
        self.rating = rating

    @classmethod
    def create_table(cls):
         '''This is going to create a movies table in our db'''

         sql_reviews = '''
            CREATE TABLE IF NOT EXISTS reviews(
                id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                user_id INTEGER,
                review_text TEXT,
                rating INTEGER,
                FOREIGN KEY (movie_id) REFERENCES movies(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''' 
         
         cursor.execute(sql_reviews)
         conn.commit()
         


         
