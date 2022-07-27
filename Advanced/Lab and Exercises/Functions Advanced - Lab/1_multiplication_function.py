# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and returns the result of the multiplication of all of them. 
# Submit only your function in the Judge system.


def multiply(*args):
    result = 1
    for i in range(len(args)):
        result *= args[i]
    return result
