# Create a class Stack which can store only strings and has the following functionality:
# •	Instance attribute: data: list
# •	Method: push(element) – adds an element at the end of the stack
# •	Method: pop() – removes and returns the last element in the stack
# •	Method: top() - returns a reference to the top most element of the stack
# •	Method: is_empty() - returns boolean True/False
# •	Override the string method to return the stack data in the format: 
# "[{element(N)}, {element(N-1)} ... {element(0)}]"

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return f"{self.data[-1]}"

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"
