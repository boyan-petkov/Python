# class IntegerList:
#     def __init__(self, *args):
#         self.__data = []
#         for x in args:
#             if type(x) == int:
#                 self.__data.append(x)
 
#     def get_data(self):
#         return self.__data
 
#     def add(self, element):
#         if not type(element) == int:
#             raise ValueError("Element is not Integer")
#         self.get_data().append(element)
#         return self.get_data()
 
#     def remove_index(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         a = self.get_data()[index]
#         del self.get_data()[index]
#         return a
 
#     def get(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         return self.get_data()[index]
 
#     def insert(self, index, el):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         elif not type(el) == int:
#             raise ValueError("Element is not Integer")
 
#         self.get_data().insert(index, el)
 
#     def get_biggest(self):
#         a = sorted(self.get_data(), reverse=True)
#         return a[0]
 
#     def get_index(self, el):
#         return self.get_data().index(el)
    
    
# You are provided with a class IntegerList. It should only store integers. The initial integers should be set by constructor.
# They are stored as a list. IntegerList has a functionality to add, remove_index, get, insert, get the biggest number and get the index of an element. 
# Your task is to test the class.
# Note: You are not allowed to change the structure of the provided code

# Constraints
# •	add operation, should add an element and returns the list.
# o	If the element is not an integer, a ValueError is thrown
# •	remove_index operation removes the element on that index and returns it.
# o	If the index is out of range, an IndexError is thrown
# •	__init__ should only take integers, and store them
# •	get should return the specific element
# o	If the index is out of range, an IndexError is thrown
# •	insert
# o	If the index is out of range, IndexError is thrown
# o	If the element is not an integer, ValueError is thrown
# •	get_biggest
# •	get_index
# Hint
# Do not forget to test the constructor



from unittest import TestCase, main


class TestList(TestCase):
    # def test_if_initialized_correctly(self):
    #     test_list = IntegerList(1, 2, 3, "a")
    #     self.assertEqual(3, len(test_list.get_data()))

    def test_get_data_method(self):
        test_list = IntegerList(1, 2, 3, "a")
        expected, actual = [1, 2, 3], test_list.get_data()
        self.assertEqual(expected, actual)

    def test_if_add_method_raises(self):
        test_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            test_list.add("a")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_if_add_method_adds_elements(self):
        test_list = IntegerList(1, 2, 3)
        test_list.add(4)
        self.assertTrue(4 in test_list.get_data())
        # self.assertEqual(4, len(test_list.get_data()))

    def test_remove_index_method_raises(self):
        test_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            test_list.remove_index(3)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_if_remove_method_really_removes(self):
        test_list = IntegerList(1, 2, 3)
        test_list.remove_index(0)
        self.assertEqual(2, len(test_list.get_data()))

    def test_get_method_raises(self):
        test_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            test_list.get(5)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_method_behavior(self):
        test_list = IntegerList(1, 2, 3)
        self.assertEqual(2, test_list.get(1))

    def test_insert_method_index_error_raises(self):
        test_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            test_list.insert(5, 5)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_method_value_error_raises(self):
        test_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            test_list.insert(1, "a")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_method_behavior(self):
        test_list = IntegerList(1, 2, 3)
        test_list.insert(0, 10)
        self.assertEqual([10, 1, 2, 3], test_list.get_data())

    def test_get_biggest_method_behavior(self):
        test_list = IntegerList(1, 2, 3)
        self.assertEqual(3, test_list.get_biggest())

    def test_get_index_method(self):
        test_list = IntegerList(1, 2, 3)
        temp = test_list.get_index(3)
        self.assertEqual(2, temp)

if __name__ == "__main__":
    main()
