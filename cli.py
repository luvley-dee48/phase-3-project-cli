from database.connection import conn, cursor
from lib.model.movies import Movies
from lib.model.reviews import Reviews
from lib.model.users import Users

def main_menu():
    while True:
        print("\n ********* Main Menu ***********")
        print("1. Manage the Users")
        print("2. Manage the Movies")
        print("3. Manage the Reviews")
        print("4. Exit")

        choice = input("Select your choice: ").strip()

        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_movies()
        elif choice == '3':
            manage_reviews()
        elif choice == '4':
            print("Exiting the application. Byeeeeee!❤️")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users():
    while True:
        print("\n********* Manage Users *************")
        print("1. Create a User")
        print("2. View All Users")
        print("3. Update a User")
        print("4. Delete a User")
        print("5. View User's Reviews")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_user()
        elif choice == '2':
            view_all_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            view_user_reviews()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_movies():
    while True:
        print("\n************ Manage Movies ************")
        print("1. Create Movie")
        print("2. View All Movies")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. View Movie's Reviews")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_movie()
        elif choice == '2':
            view_all_movies()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            view_movie_reviews()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_reviews():
    while True:
        print("\n******** Manage Reviews ***********")
        print("1. Create Review")
        print("2. View All Reviews")
        print("3. Update Review")
        print("4. Delete Review")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_review()
        elif choice == '2':
            view_all_reviews()
        elif choice == '3':
            update_review()
        elif choice == '4':
            delete_review()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Functions for Users
def create_user():
    print("\n******** Create User **********")
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()

    user = Users.create(username, email, password)
    print(f"User created: {user}")

def view_all_users():
    print("\n***** All Users *******")
    users = Users.fetch_all()
    for user in users:
        print(user)

def update_user():
    print("\n****** Update User ******")
    user_id = input("Enter user ID: ").strip()
    user = Users.all.get(int(user_id))

    if user:
        user.username = input(f"Enter new username (current: {user.username}): ").strip()
        user.email = input(f"Enter new email (current: {user.email}): ").strip()
        user.password = input(f"Enter new password (current: {user.password}): ").strip()
        user.update()
        print(f"User updated: {user}")
    else:
        print("User not found.")

def delete_user():
    print("\n******** Delete User ********")
    user_id = input("Enter user ID: ").strip()
    user = Users.all.get(int(user_id))

    if user:
        user.delete()
        print(f"User deleted: {user}")
    else:
        print("User not found.")

def view_user_reviews():
    print("\n********** User's Reviews *********")
    user_id = input("Enter user ID: ").strip()
    user = Users.all.get(int(user_id))

    if user:
        sql_reviews = 'SELECT * FROM reviews WHERE user_id = ?;'
        cursor.execute(sql_reviews, (user.id,))
        reviews = cursor.fetchall()
        for review in reviews:
            print(review)
    else:
        print("User not found.")

# Functions for Movies
def create_movie():
    print("\n********* Create Movie **********")
    title = input("Enter title: ").strip()
    genre = input("Enter genre: ").strip()
    release_date = input("Enter release date (YYYY-MM-DD): ").strip()
    rating = input("Enter rating (1-10): ").strip()

    movie = Movies.create(title, genre, release_date, int(rating))
    print(f"Movie created: {movie}")

def view_all_movies():
    print("\n********* All Movies *********")
    movies = Movies.fetch_all()
    for movie in movies:
        print(movie)

def update_movie():
    print("\n******* Update Movie ********")
    movie_id = input("Enter movie ID: ").strip()
    movie = Movies.all.get(int(movie_id))

    if movie:
        movie.title = input(f"Enter new title (current: {movie.title}): ").strip()
        movie.genre = input(f"Enter new genre (current: {movie.genre}): ").strip()
        movie.release_date = input(f"Enter new release date (current: {movie.release_date}): ").strip()
        movie.rating = input(f"Enter new rating (current: {movie.rating}): ").strip()
        movie.update()
        print(f"Movie updated: {movie}")
    else:
        print("Movie not found.")

def delete_movie():
    print("\n******** Delete Movie *******")
    movie_id = input("Enter movie ID: ").strip()
    movie = Movies.all.get(int(movie_id))

    if movie:
        movie.delete()
        print(f"Movie deleted: {movie}")
    else:
        print("Movie not found.")

def view_movie_reviews():
    print("\n********* Movie's Reviews *********")
    movie_id = input("Enter movie ID: ").strip()
    movie = Movies.all.get(int(movie_id))

    if movie:
        sql_reviews = 'SELECT * FROM reviews WHERE movie_id = ?;'
        cursor.execute(sql_reviews, (movie.id,))
        reviews = cursor.fetchall()
        for review in reviews:
            print(review)
    else:
        print("Movie not found.")

# Functions for Reviews
def create_review():
    print("\n******** Create Review *******")
    movie_id = input("Enter movie ID: ").strip()
    user_id = input("Enter user ID: ").strip()
    review_text = input("Enter review text: ").strip()
    rating = input("Enter rating (1-10): ").strip()

    review = Reviews.create(int(movie_id), int(user_id), review_text, int(rating))
    print(f"Review created: {review}")

def view_all_reviews():
    print("\n********* All Reviews **********")
    sql_reviews = 'SELECT * FROM reviews;'
    cursor.execute(sql_reviews)
    reviews = cursor.fetchall()
    for review in reviews:
        print(review)

def update_review():
    print("\n****** Update Review **********")
    review_id = input("Enter review ID: ").strip()
    sql_reviews = 'SELECT * FROM reviews WHERE id = ?;'
    cursor.execute(sql_reviews, (review_id,))
    review = cursor.fetchone()

    if review:
        new_review_text = input(f"Enter new review text (current: {review[3]}): ").strip()
        new_rating = input(f"Enter new rating (current: {review[4]}): ").strip()
        sql_update = '''
            UPDATE reviews SET review_text = ?, rating = ? WHERE id = ?
        '''
        cursor.execute(sql_update, (new_review_text, new_rating, review_id))
        conn.commit()
        print(f"Review updated: ID {review_id}")
    else:
        print("Review not found.")

def delete_review():
    print("\n******* Delete Review ********")
    review_id = input("Enter review ID: ").strip()
    sql_reviews = 'DELETE FROM reviews WHERE id = ?;'
    cursor.execute(sql_reviews, (review_id,))
    conn.commit()
    print(f"Review deleted: ID {review_id}")


main_menu()