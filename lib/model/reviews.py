from database.connection import conn, cursor
# It defines the Reviews class
class Reviews:
    # Class variable acting as a dictionary to store review objects by their IDs.
    
    all = {}
    # Constructor for the Reviews class. 
    def __init__(self,movie_id,user_id,review_text,rating,id=None):
        self.id = id
        self.movie_id = movie_id
        self.user_id = user_id
        self.review_text = review_text
        self.rating = rating

    # This method creates the "reviews" table in the database if it doesn't exist. 
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

    # this method drops the table
    @classmethod
    def drop_table(cls):
        sql_reviews = '''
            DROP TABLE IF EXISTS reviews;
        '''
        
        cursor.execute(sql_reviews)
        conn.commit()

    # This method saves the review object to the database.
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
        type(self).all[self.id] = self
        
    # This class method is a factory for creating new review objects. 
    @classmethod
    def create(cls, movie_id, use_id, review_text, rating):
        reviews = cls(movie_id, use_id, review_text, rating) 

        #  saving the instances in the db
        reviews.save()

        return reviews
    #  This method updates an existing review record in the database based on the object. 
    def update(self):
        '''This updates an existing movie record in the database.'''
        sql_reviews = '''
            UPDATE reviews SET movie_id = ?, user_id = ?, review_text= ?, rating = ? WHERE id = ?
        '''
        cursor.execute(sql_reviews, (self.movie_id, self.user_id, self.review_text, self.rating, self.id))
        conn.commit()

    # This method deletes the review record associated with the object from the database.

    def delete(self):
        sql_reviews = '''
            DELETE FROM reviews WHERE id = ?;

        '''
        cursor.execute(sql_reviews, (self.id,))
        conn.commit()
    # This method defines how the object is represented as a string 
    def __repr__(self):
        return f"< Reviews{self.movie_id} {self.user_id} {self.review_text} {self.rating} >"
    
    # This class method takes a database row (tuple) and tries to find a corresponding review object in the all dictionary using the ID.

    @classmethod
    def instance_from_db(cls, row):
        '''Create a user instance from a database row'''
        review = cls.all.get(row[0])
        if review:
            review.movie_id = row[1]
            review.user_id = row[2]
            review.review_text = row[3]
            review.rating = row[4]
        else:
            review = cls(row[1], row[2], row[3],row[4])
            review.id = row[0]
            cls.all[review.id] = review
        return review
    
      # Property for movie_id with validation
    @property
    def movie_id(self):
        return self._movie_id

    @movie_id.setter
    def movie_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Movie ID must be an integer.")
        self._movie_id = value

    # Property for user_id with validation
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = value

    # Property for review_text with validation
    @property
    def review_text(self):
        return self._review_text

    @review_text.setter
    def review_text(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Review text must be a non-empty string.")
        self._review_text = value.strip()

         
    # This class method takes a database row (tuple) and tries to find a corresponding review object in the all dictionary using the ID.

    @classmethod
    def find_by_id(cls, review_id):
        '''Find a review by its ID.'''
        sql_reviews = '''
            SELECT * FROM reviews WHERE id = ?;
        '''
        cursor.execute(sql_reviews, (review_id,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    # This class method retrieves reviews associated with a specific movie ID.
    @classmethod
    def find_by_movie_id(cls, movie_id):
        '''Find reviews by movie ID.'''
        sql_reviews = '''
            SELECT * FROM reviews WHERE movie_id = ?;
        '''
        cursor.execute(sql_reviews, (movie_id,))
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    # This class method retrieves reviews associated with a specific user ID.
    @classmethod
    def find_by_user_id(cls, user_id):
        '''Find reviews by user ID.'''
        sql_reviews = '''
            SELECT * FROM reviews WHERE user_id = ?;
        '''
        cursor.execute(sql_reviews, (user_id,))
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]
    
    


    


         
