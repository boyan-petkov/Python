# class Cat:

#   def __init__(self, name):
#     self.name = name
#     self.fed = False
#     self.sleepy = False
#     self.size = 0

#   def eat(self):
#     if self.fed:
#       raise Exception('Already fed.')

#     self.fed = True
#     self.sleepy = True
#     self.size += 1

#   def sleep(self):
#     if not self.fed:
#       raise Exception('Cannot sleep while hungry')

#     self.sleepy = False


# Create a class CatTests
# In judge you need to submit just the CatTests class, with the unitttest module imported.
# Create the following tests:
# •	Cat's size is increased after eating
# •	Cat is fed after eating
# •	Cat cannot eat if already fed, raises an error
# •	Cat cannot fall asleep if not fed, raises an error
# •	Cat is not sleepy after sleeping
# Hints
# Follow the logic of the previous problem

from unittest import TestCase, main
class CatTests(TestCase):
    def test_if_correctly_initialized(self):
        cat = Cat("Leon")
        self.assertEqual("Leon", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_if_cat_size_increased_after_eating(self):
        cat = Cat("Leon")
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_attributes_after_eating(self):
        cat = Cat("Leon")
        cat.eat()
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)

    def test_if_error_is_raises_with_eat_method_after_eating(self):
        with self.assertRaises(Exception) as error:
            cat = Cat("Leon")
            cat.eat()
            cat.eat()
        expected_msg = 'Already fed.'
        self.assertEqual(expected_msg, str(error.exception))

    def test_if_try_sleep_hungry_exception_raised(self):
        with self.assertRaises(Exception) as error:
            cat = Cat("Leon")
            cat.sleep()
        expected = 'Cannot sleep while hungry'
        self.assertEqual(expected, str(error.exception))

    def test_if_cat_sleepy_after_sleep(self):
        cat = Cat("Leon")
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()

    
