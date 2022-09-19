from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscriptions: Subscription):
        if subscriptions not in self.subscriptions:
            self.subscriptions.append(subscriptions)

    def subscription_info(self, subscription_id: int):
        customer = Gym.get_info_by_id(subscription_id, self.customers)
        subscription = Gym.get_info_by_id(subscription_id, self.subscriptions)
        trainer = Gym.get_info_by_id(subscription_id, self.trainers)
        equipment = Gym.get_info_by_id(subscription_id, self.equipment)
        plan = Gym.get_info_by_id(subscription_id, self.plans)

        return f"{repr(subscription)}\n{repr(customer)}\n{repr(trainer)}\n{repr(equipment)}\n{repr(plan)}"

    @staticmethod
    def get_info_by_id(subscription_id, list_of_objects):
        for object_ in list_of_objects:
            if object_.id == subscription_id:
                return object_
