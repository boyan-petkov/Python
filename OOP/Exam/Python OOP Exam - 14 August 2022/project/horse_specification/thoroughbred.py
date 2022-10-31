from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def maximum_speed(self):
        return 140

    def train(self):
        current = self.speed
        maximum = self.maximum_speed()
        train_points = 3
        if current + train_points > maximum:
            self.speed = maximum
        else:
            self.speed += train_points

