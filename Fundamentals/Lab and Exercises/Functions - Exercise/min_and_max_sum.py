# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. 
# Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

def my_function(nums):
    minimum = min((nums))
    maximum = max((nums))
    total_sum = sum((nums))
    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {total_sum}")


numbers = [int(el) for el in input().split()]
my_function(numbers)
