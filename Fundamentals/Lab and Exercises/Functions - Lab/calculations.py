# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it. 
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. 
# The operator can be one of the following:  
# "multiply", "divide", "add", "subtract". 

def calculate_numbers(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return num1 / num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


input_operator, number_1, number_2 = input(), int(input()), int(input())

print(int(calculate_numbers(input_operator, number_1, number_2)))
