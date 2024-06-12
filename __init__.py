from lib.model.movies import Movies


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

# # all_movies = Movies.fetch_all()

# for movie in all_movies:
#     print(movie)
# print(Movies.all)

# movies1.save()
# movies2.save()
# movies3.save()
# movies4.save()
# movies5.save()
# movies6.save()
# movies7.save() 
