
# Create a class called reverse_iter which should receive an iterable upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.

class reverse_iter:
    def __init__(self, object_list):
        self.object_list = object_list
        self.start = len(object_list) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.object_list[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
