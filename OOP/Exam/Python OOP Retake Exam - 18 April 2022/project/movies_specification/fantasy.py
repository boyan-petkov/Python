from project.movie_specification.movie import Movie
from project.movie_specification.movie import validate_age_restriction_


class Fantasy(Movie):
    __AGE_RESTRICTION = 6
    __AGE_RESTRICTION_MESSAGE = "Fantasy movies must be restricted for audience under 6 years!"

    def __init__(self, title: str, year: int, owner: object, age_restriction=__AGE_RESTRICTION):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        validate_age_restriction_(value, self.__AGE_RESTRICTION, self.__AGE_RESTRICTION_MESSAGE)
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"

