
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseFabric:
    @staticmethod
    def create_horse(value, name, speed):
        if value == "Appaloosa":
            return Appaloosa(name, speed)
        if value == "Thoroughbred":
            return Thoroughbred(name, speed)


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __get_horse_by_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return horse

    def __get_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __get_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse_exists = self.__get_horse_by_name(horse_name)
        if horse_exists:
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = HorseFabric.create_horse(horse_type, horse_name, horse_speed)
        if horse:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_exists = self.__get_jockey_by_name(jockey_name)
        if jockey_exists:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race_exists = self.__get_race_by_type(race_type)
        if race_exists:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def __get_last_added_horse_by_type(self, horse_type):
        for index in range(len(self.horses) - 1, -1, -1):
            current = self.horses[index]
            if current.get_horse_type() == horse_type and current.is_taken is False:
                return current

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.__get_last_added_horse_by_type(horse_type)
        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__get_race_by_type(race_type)
        jockey = self.__get_jockey_by_name(jockey_name)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__get_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        participants = {}
        for participant in race.jockeys:
            jockey_name = participant.name
            speed = participant.horse.speed
            horse_name = participant.horse.name
            participants[speed] = [horse_name, jockey_name]
        participants = tuple(sorted(participants.items()))
        best = participants[len(participants) - 1]
        jockey, horse, speed = best[1][1], best[1][0], best[0]

        return f"The winner of the {race_type} race, with a speed of {speed}km/h " \
               f"is {jockey}! Winner's horse: {horse}."










