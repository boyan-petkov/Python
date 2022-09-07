
from project.animal import Animal
from project.worker import Worker


def add_to_result(list_type):
    curr_result = ""
    for animal in list_type:
        curr_result += repr(animal) + "\n"
    return curr_result


class Zoo:
    def __init__(self, name, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary
        if needed_money > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care
        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        cheetahs = []
        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
        result += f"----- {len(lions)} Lions:\n"
        result += add_to_result(lions)
        result += f"----- {len(tigers)} Tigers:\n"
        result += add_to_result(tigers)
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += add_to_result(cheetahs)
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)
        result += f"----- {len(keepers)} Keepers:\n"
        result += add_to_result(keepers)
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += add_to_result(caretakers)
        result += f"----- {len(vets)} Vets:\n"
        result += add_to_result(vets)
        return result.strip()

