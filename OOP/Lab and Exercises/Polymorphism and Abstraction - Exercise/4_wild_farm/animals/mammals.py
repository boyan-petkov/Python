
from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ["Fruit", "Vegetable"]
    WEIGHT_INCREMENTAL = 0.1

    def make_sound(self):
        return "Squeak"



class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = ["Meat", "Vegetable"]
    WEIGHT_INCREMENTAL = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENTAL = 1

    def make_sound(self):
        return "ROAR!!!"
