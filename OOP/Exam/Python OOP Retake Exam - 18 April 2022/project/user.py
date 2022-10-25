def is_empty_or_whitespace(value):
    return not value or not value.strip()


class User:
    __INVALID_USERNAME = "Invalid username!"
    ___INVALID_AGE = "Users under the age of 6 are not allowed!"

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @classmethod
    def __validate_username(cls, value):
        if is_empty_or_whitespace(value):
            raise ValueError(cls.__INVALID_USERNAME)

    @classmethod
    def __validate_age(cls, value):
        if value < 6:
            raise ValueError(cls.___INVALID_AGE)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def __str__(self):
        result_str = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']
        if len(self.movies_liked) > 0:
            for liked in self.movies_liked:
                result_str.append(liked.details())
        else:
            result_str.append('No movies liked.')
        result_str.append('Owned movies:')
        if len(self.movies_owned) > 0:
            for owned in self.movies_owned:
                result_str.append(owned.details())
        else:
            result_str.append('No movies owned.')
        return '\n'.join(result_str)


