# class Car:
#     def __init__(self, make, model, fuel_consumption, fuel_capacity):
#         self.make = make
#         self.model = model
#         self.fuel_consumption = fuel_consumption
#         self.fuel_capacity = fuel_capacity
#         self.fuel_amount = 0
    
#     @property
#     def make(self):
#         return self.__make
    
#     @make.setter
#     def make(self, new_value):
#         if not new_value:
#             raise Exception("Make cannot be null or empty!")
#         self.__make = new_value

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self, new_value):
#         if not new_value:
#             raise Exception("Model cannot be null or empty!")
#         self.__model = new_value

#     @property
#     def fuel_consumption(self):
#         return self.__fuel_consumption
    
#     @fuel_consumption.setter
#     def fuel_consumption(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel consumption cannot be zero or negative!")
#         self.__fuel_consumption = new_value

#     @property
#     def fuel_capacity(self):
#         return self.__fuel_capacity
    
#     @fuel_capacity.setter
#     def fuel_capacity(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel capacity cannot be zero or negative!")
#         self.__fuel_capacity = new_value

#     @property
#     def fuel_amount(self):
#         return self.__fuel_amount
    
#     @fuel_amount.setter
#     def fuel_amount(self, new_value):
#         if new_value < 0:
#             raise Exception("Fuel amount cannot be negative!")
#         self.__fuel_amount = new_value

#     def refuel(self, fuel):
#         if fuel <= 0:
#             raise Exception("Fuel amount cannot be zero or negative!")
#         self.__fuel_amount += fuel
#         if self.__fuel_amount > self.__fuel_capacity:
#             self.__fuel_amount = self.__fuel_capacity

#     def drive(self, distance):
#         needed = (distance / 100) * self.__fuel_consumption

#         if needed > self.__fuel_amount:
#             raise Exception("You don't have enough fuel to drive!")

#         self.__fuel_amount -= needed

# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

# You are provided with a simple project containing only one class - Car. 
# The provided class is simple - its main point is to represent some of the functionality of a Car. 
# Each car contains information about its make, model, fuel consumption, fuel amount and fuel capacity.
# Also, each Car can add some fuel to its tank by refueling and can travel distance by driving. In order to be driven, our Car needs to have enough fuel. 
# Everything in the provided skeleton is working perfectly fine and you mustn't change it.
# Your job now is to write unit tests on the provided project and its functionality. You should test every part of code inside the Car class:
# •	You should test the constructor
# •	You should test all the methods and validations inside the class
# Constraints
# •	Everything in the provided skeleton is working perfectly fine
# •	You mustn't change anything in the project structure
# •	Any part of validation should be tested
# •	There is no limit on the tests you can write but keep your attention on the main functionality
# Note: You are not allowed to change the structure of the provided code

from unittest import TestCase, main

class CarTesting(TestCase):
    def test_if_initialized_correctly(self):
        car = Car("bmw", "f11", 15, 60)
        self.assertEqual("bmw", car.make)
        self.assertEqual("f11", car.model)
        self.assertEqual(15, car.fuel_consumption)
        self.assertEqual(60, car.fuel_capacity)

    def test_when_make_empy_raises(self):
        with self.assertRaises(Exception) as error:
            car = Car("", "f11", 15, 60)
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_when_model_empy_raises(self):
        with self.assertRaises(Exception) as error:
            car = Car("BMW", "", 15, 60)
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_when_consumption_is_zero_raises(self):
        with self.assertRaises(Exception) as error:
            car = Car("bmw", "f11", 0, 60)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_when_capacity_is_zero_raises(self):
        with self.assertRaises(Exception) as error:
            car = Car("bmw", "f11", 15, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_when_fuel_amount_is_zero_raises(self):
        car = Car("bmw", "f11", 15, 60)
        with self.assertRaises(Exception) as error:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_if_refuel_method_raises(self):
        car = Car("bmw", "f11", 15, 60)
        with self.assertRaises(Exception) as error:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel_normal_behavior(self):
        car = Car("bmw", "f11", 15, 60)
        car.refuel(30)
        self.assertEqual(30, car.fuel_amount)
        car.refuel(10)
        self.assertEqual(40, car.fuel_amount)

    def test_refuel_when_overfilled(self):
        car = Car("bmw", "f11", 15, 60)
        car.refuel(65)
        self.assertEqual(60, car.fuel_amount)

    def test_if_drive_method_raises(self):
        car = Car("bmw", "f11", 15, 60)
        with self.assertRaises(Exception) as error:
            car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(error.exception))

    def test_drive_method_behavior(self):
        car = Car("bmw", "f11", 15, 60)
        car.fuel_amount = 50
        car.drive(200)

        self.assertEqual(20, car.fuel_amount )

if __name__ == "__main__":
    main()
    
    


