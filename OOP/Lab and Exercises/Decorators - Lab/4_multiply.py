
# Having the following code:
#   def multiply(times):

#     def decorator(function):

#         # TODO: Implement

#     return decorator
  
# Complete the code so it works as expected

# Test Code                      Output
# @multiply(3)                   39
# def add_ten(number):
#     return number + 10

# print(add_ten(3))


def multiply(n):
    def decorator(function):
        def wrapper(number):
            temp = function(number)
            res = temp * n
            return res
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
