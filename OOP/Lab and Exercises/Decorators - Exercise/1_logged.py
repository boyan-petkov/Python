# Create a decorator called logged. It should return the name of the function that is being called and its parameters. 
# It should also return the result of the execution of the function being called. See the examples for more clarification.

def logged(function):
    def wrapper(*args):
        retval = f'you called {function.__name__}{args}\n'
        retval += f'it returned {function(*args)}'
        return retval
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(func(4, 4, 4))
print(sum_func(1, 4))
