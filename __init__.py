from lib.model.movies import Movies
from lib.model.reviews import Reviews
from lib.model.users import Users

Movies.drop_table()
Movies.create_table()


movies1 = Movies.create ("Blindspot", "Investigative and crime", "2015-2020", "7.3/10")

movies1.rating = "7.4/10"

movies1.update()

movies2 = Movies.create("The Lincoln Lawyer", "Legal thriller", "2022", "7.7/10")
movies3 = Movies.create("The last Ship", "Action Thriller", "2016", "7.4/10")
movies4 = Movies.create("Damsel", "Dark fantacy", "2024", "6.1/10")
movies5 = Movies.create("The letter for the King", "Fantacy adventure", "2020", "6/10")
movies6 = Movies.create("The Shooter", "Conspiracy Thriller", "2016-2018", "8.3/10")
movies7 = Movies.create("Lethal Weapon", "Comedy-drama", "2016-2019", "9.0/10")
movies8 = Movies.create("Princess switch", "Comedy", "2018", "6.1/10")

# movies8.delete()

# all_movies = Movies.fetch_all()

# for movie in all_movies:
#     print(movie)
 
# movies1.save()
# movies2.save()
# movies3.save()
# movies4.save()
# movies5.save()
# movies6.save()
# movies7.save() 


Reviews.drop_table()
Reviews.create_table()

review1 = Reviews.create(movies1.id, 6,"Great show..... Unfortunate they have fired the actor that makes it great.", "9/10")
review2 = Reviews.create(movies2.id, 1,"Very disappointing.Seasons 1 & 2 were entertaining but season 3 was kinda boring.", "6/10")
review3 = Reviews.create(movies3.id,  4,"Lots of fun for a casual movie night!", "7/10")
review3 = Reviews.create(movies4.id, 7, "Great series, want more!", "8/10")
review3 = Reviews.create(movies5.id, 3, "Action Packed and very entertaining.", "5/10")
review3 = Reviews.create(movies6.id, 5, "Nice series, terrible ending", "7/10")
review3 = Reviews.create(movies7.id, 2, "Loved the Movie, Ep 3 finally got it right!", "7.4/10")

Users.drop_table()
Users.create_table()

user1 = Users.create("Mk","mutisyamoses722@gmail.com","mkblueband")
user2 = Users.create("Gee","geetheelegend@gmail.com","geeprado")
user3 = Users.create("Althea","twinkegrand@gmail.com","Musical")
user4 = Users.create("Rubie", "hilzrubie@gmail.com", "Addie123")
user5 = Users.create("Jones","jones21@gmail.com","jn123")
user6 = Users.create("Kelvin","kelvin@gmail.com","thirdlife6")
user7 = Users.create("Sharon","sharon12@gmail.com","roadtrip")
