# class Worker:

#   def __init__(self, name, salary, energy):
#     self.name = name
#     self.salary = salary
#     self.energy = energy
#     self.money = 0

#   def work(self):
#     if self.energy <= 0:
#         raise Exception('Not enough energy.')

#     self.money += self.salary
#     self.energy -= 1

#   def rest(self):
#     self.energy += 1

#   def get_info(self):
#     return (f'{self.name} has saved {self.money} money.')

# Create a class WorkerTests
# In judge you need to submit just the WokerTests class, with the unitttest module imported.
# Create the following tests:
# •	Test if the worker is initialized with correct name, salary and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called	
# •	Test if the get_info method returns the proper string with correct values

import unittest


class WorkerTests(unittest.TestCase):
    def test_if_worker_initialized(self):
        worker = Worker("Boyan", 2000, 20)
        self.assertEqual("Boyan", worker.name)
        self.assertEqual(2000, worker.salary)
        self.assertEqual(20, worker.energy)

    def test_if_energy_increased_after_rest(self):
        worker = Worker("Boyan", 2000, 20)
        self.assertEqual(20, worker.energy)
        worker.rest()
        self.assertEqual(21, worker.energy)

    def test_worker_tries_working_with_negative_energy(self):
        worker = Worker("Boyan", 2000, -1)
        with self.assertRaises(Exception) as error:
            worker.work()
        self.assertEqual('Not enough energy.', str(error.exception))

    def test_worker_tries_working_with_zero_energy(self):
        worker = Worker("Boyan", 2000, 0)
        with self.assertRaises(Exception) as error:
            worker.work()
        self.assertEqual('Not enough energy.', str(error.exception))

    def test_if_money_increased_after_working(self):
        worker = Worker("Boyan", 2000, 20)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(2000, worker.money)
        worker.work()
        self.assertEqual(4000, worker.money)

    def test_if_energy_decreased_after_working(self):
        worker = Worker("Boyan", 2000, 20)
        worker.work()
        self.assertEqual(19, worker.energy)

    def test_get_info_method(self):
        worker = Worker("Boyan", 2000, 20)
        worker.work()
        expected = 'Boyan has saved 2000 money.'
        actual = worker.get_info()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

