# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple numbers (integers) as additional arguments (*args). 
# The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below. 
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

def operate(operator, *args):
    result = 0
    if operator in "-+":
        result = 0
    else:
        result = 1

    if operator == "+":
        for num in args:
            result += num
    elif operator == "-":
        for num in args:
            result -= num
    elif operator == "/":
        for num in args:
            result /= num
    elif operator == "*":
        for num in args:
            result *= num
    return result
