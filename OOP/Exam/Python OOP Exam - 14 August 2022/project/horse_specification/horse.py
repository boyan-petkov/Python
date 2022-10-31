
from abc import ABC, abstractmethod


class Horse(ABC):
    __SPEED_TO_HIGH_MSG = "Horse speed is too high!"

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @abstractmethod
    def maximum_speed(self):
        return 0

    @staticmethod
    def __validate_name(value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

    def __validate_speed(self, value):
        if value > self.maximum_speed():
            raise ValueError(self.__SPEED_TO_HIGH_MSG)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__validate_speed(value)
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

    def get_horse_type(self):
        return self.__class__.__name__



