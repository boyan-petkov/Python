
from abc import ABC, abstractmethod
from project.user import is_empty_or_whitespace, User


def validate_age_restriction_(value_passed, value_restriction, msg):
    if value_passed < value_restriction:
        raise ValueError(msg)


class Movie(ABC):
    __INVALID_TITLE = "The title cannot be empty string!"
    __INVALID_YEAR = "Movies weren't made before 1888!"
    __INVALID_OWNER = "The owner must be an object of type User!"
    __YEAR_FIRST_MOVIE = 1888

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @classmethod
    def __validate_title(cls, value):
        if is_empty_or_whitespace(value):
            raise ValueError(cls.__INVALID_TITLE)

    @classmethod
    def __validate_owner(cls, value):
        if not isinstance(value, User):
            raise ValueError(cls.__INVALID_OWNER)

    @classmethod
    def __validate_year(cls, value):
        if value < cls.__YEAR_FIRST_MOVIE:
            raise ValueError(cls.__INVALID_YEAR)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__validate_owner(value)
        self.__owner = value

    @abstractmethod
    def details(self):
        pass
