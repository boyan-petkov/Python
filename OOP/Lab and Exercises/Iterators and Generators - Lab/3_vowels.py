
# Create a class called vowels which should receive a stirng.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.

class vowels:
    __VALID_VOWELS = ["A", "E", "I", "O", "Y", "U", "a", "e", "i", "o", "y", "u"]

    def __get_vowels(self):
        vowels = [el for el in self.text if el in self.__VALID_VOWELS ]
        return vowels

    def __init__(self, text):
        self.text = text
        self.filtered = self.__get_vowels()
        self.start = 0
        self.end = len(self.filtered) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        i = self.start
        self.start += 1
        return self.filtered[i]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
