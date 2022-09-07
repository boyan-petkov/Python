from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender: str, age: int):
        super().__init__(name, gender, age, 45)

