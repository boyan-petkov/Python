# Create a decorator function called even_parameters. 
# It should check if all parameters passed to a function are even numbers and only then execute the function and return the result. 
# Otherwise, don't execute the function and return "Please use only even numbers!"


def even_parameters(func):
    def wrapper(*args):
        if any(arg % 2 != 0 if type(arg) == int else True for arg in args):
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
