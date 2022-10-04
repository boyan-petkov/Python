# Create a class called take_skip. Upon initialization it should receive a step (number) and a count (number). 
# Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.
# For more clarification, see the examples:

class take_skip:
    def __init__(self, step, count):
        self.start = 0
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        temp = self.start
        self.start += self.step
        self.counter += 1
        return temp

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
