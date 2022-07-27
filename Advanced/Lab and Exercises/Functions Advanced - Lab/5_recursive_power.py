# Create a recursive function called recursive_power() which should receive a number and a power.
# Using recursion, return the result of number ** power. Submit only the function in the judge system.

def recursive_power(num, power):
    result = 1
    if power == 0:
        return result
    result = num * recursive_power(num, power - 1)
    return result
