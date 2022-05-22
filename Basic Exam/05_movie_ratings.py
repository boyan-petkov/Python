from sys import maxsize
movies_number = int(input())

best_rating = -maxsize
lowest_rating = maxsize
best_movie = ""
worst_movie = ""
rating = 0
counter = 0
for movies in range(movies_number):
    movie_name = input()
    rating_movies = float(input())
    rating += rating_movies
    counter += 1
    if rating_movies > best_rating:
        best_rating = rating_movies
        best_movie = movie_name
    if rating_movies < lowest_rating:
        lowest_rating = rating_movies
        worst_movie = movie_name
average = rating / counter
print(f"{best_movie} is with highest rating: {best_rating}")
print(f"{worst_movie} is with lowest rating: {lowest_rating}")
print(f"Average rating: {average:.1f}")

