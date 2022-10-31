
class HorseRace:
    __VALID_RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]
    __INVALID_RACE_TYPE_MSG = "Race type does not exist!"

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    def __validate_race_type(self, value):
        if value not in self.__VALID_RACE_TYPES:
            raise ValueError(self.__INVALID_RACE_TYPE_MSG)

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        self.__validate_race_type(value)
        self.__race_type = value
