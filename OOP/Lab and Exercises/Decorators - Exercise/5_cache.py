# Create a decorator called cache. It should store all the returned values of the recursive function fibonacci. You are provided with this code:
# You need to create a dictionary called log that will store all the n's (keys) and the returned results (values) and 
# attach that dictionary to the fibonacci function as a variable called log, so when you call it, it returns that dictionary.
# For more clarification, see the examples

class Cache:

    def __init__(self, func):
        self.func = func
        self.log = {}

    def __call__(self, n):
        self.log[n] = self.func(n)
        return self.func(n)


def cache(func):
    def wrapper(arg):
        wrapper.log.update({arg: func(arg)})
        return func(arg)
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)
print(fibonacci.log)
