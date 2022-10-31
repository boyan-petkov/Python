
def is_empty_or_whitespace(value):
    return not value or not value.strip()


class Jockey:
    __INVALID_NAME_MSG = "Name should contain at least one character!"
    __INVALID_AGE_MSG = "Jockeys must be at least 18 to participate in the race!"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    def __validate_name(self, value):
        if is_empty_or_whitespace(value):
            raise ValueError(self.__INVALID_NAME_MSG)

    def __validate_age(self, value):
        if value < 18:
            raise ValueError(self.__INVALID_AGE_MSG)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
