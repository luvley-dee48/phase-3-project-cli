import sqlite3 
conn = sqlite3.connect("database/Entertainment.db")

cursor = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        release_date TIMESTAMP,
        rating INTEGER
    )
'''

sql_users = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT
    )
'''

sql_reviews = '''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        user_id INTEGER,
        review_text TEXT,
        rating INTEGER,
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
'''

cursor.execute(sql)
cursor.execute(sql_users)
cursor.execute(sql_reviews)

conn.commit()
conn.close()

