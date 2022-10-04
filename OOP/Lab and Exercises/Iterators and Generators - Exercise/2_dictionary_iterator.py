
# Create a class called dictionary_iter. Upon initialization it should receive a dictionary object. 
# Implement the iterator, so it returns each key-value pair of the dictionary as a tuple of two elements (the key and the value).

class dictionary_iter:
    def __init__(self, some_dict):
        self.some_dict = list(some_dict.items())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not (self.count < len(self.some_dict)):
            raise StopIteration
        res = self.some_dict[self.count]
        self.count += 1
        return res


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
