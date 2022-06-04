# You will receive three integer numbers. 
# Write functions named:
# •	sum_numbers() that returns the sum of the first two integers
# •	subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters. 
# Print the result of the subtract() function on the console.


def add_and_subtract(first_num, second_num, third_num):
    def sum_numbers():
        return first_num + second_num

    def subtract():
        return sum_numbers() - third_num

    return subtract()


num1, num2, num3 = int(input()), int(input()), int(input()),
print(add_and_subtract(num1, num2, num3))
