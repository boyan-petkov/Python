
from project.movie_specification.movie import Movie
from project.user import User


def get_user_by_username(name, collection):
    for user in collection:
        if user.username == name:
            return user


# def create_user_instance(name, age):

class MovieApp:
    __USER_EXISTS_MSG = "User already exists!"
    __USER_NOT_REGISTERED_MSG = "This user does not exist!"
    __MOVIE_ALREADY_UPLOADED = "Movie already added to the collection!"

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = get_user_by_username(username, self.users_collection)
        if user in self.users_collection:
            raise Exception(self.__USER_EXISTS_MSG)

        user_create = User(username, age)
        self.users_collection.append(user_create)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = get_user_by_username(username, self.users_collection)
        if user not in self.users_collection:
            raise Exception(self.__USER_NOT_REGISTERED_MSG)

        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception(self.__MOVIE_ALREADY_UPLOADED)

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = get_user_by_username(username, self.users_collection)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)
        return f'{username} successfully edited {movie.title} movie.'

        # TODO

    def delete_movie(self, username: str, movie: Movie):
        user = get_user_by_username(username, self.users_collection)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."  # CHECK IS IT WORKING PROPERLY

    def like_movie(self, username, movie: Movie):
        user = get_user_by_username(username, self.users_collection)
        if user.username == movie.owner.username:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = get_user_by_username(username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())
        return '\n'.join(result)

    def __str__(self):
        result = ""
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join([u.username for u in self.users_collection])}\n"
        if not self.movies_collection:
            result += "All movies: No movies.\n"
        else:
            result += f"All movies: {', '.join([m.title for m in self.movies_collection])}\n"
        return result.strip()


