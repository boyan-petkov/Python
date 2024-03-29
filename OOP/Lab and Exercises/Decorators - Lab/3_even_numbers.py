
# Having the following code:

# def even_numbers(function):

#     def wrapper(numbers):

#         # TODO: Implement

#     return wrapper

# Complete the code so it works as expected
 
# Input                                                 Output
# @even_numbers                                          [2, 4]
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))      

def even_numbers(function):
    def wrapper(numbers):
        res = [n for n in numbers if n % 2 == 0]
        return function(res)
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
