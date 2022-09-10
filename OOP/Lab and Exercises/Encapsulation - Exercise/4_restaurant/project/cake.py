from project.food.dessert import Dessert


class Cake(Dessert):
    PRICE = 5
    GRAMS  = 250
    CALORIES = 1000

    def __init__(self, name):
        super().__init__(name,Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
