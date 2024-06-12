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


    @classmethod
    def drop_table(cls):
        sql_reviews = '''
            DROP TABLE IF EXISTS reviews;
        '''
        
        cursor.execute(sql_reviews)
        conn.commit()

        
    def save(self):
        sql_reviews = '''
            INSERT INTO reviews (
                movie_id,
                user_id,
                review_text,
                rating
            ) VALUES (? ,? ,? ,?);
        '''
        cursor.execute(sql_reviews,(self.movie_id, self.user_id, self.review_text, self.rating),)

        conn.commit()

        self.id = cursor.lastrowid
        

    @classmethod
    def create(cls, movie_id, use_id, review_text, rating):
        reviews = cls(movie_id, use_id, review_text, rating) 

        #  saving the instances in the db
        reviews.save()

        return reviews

    


         
