# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and 
# prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

number = list(map(int, input().split(", ")))

group = 0

numbers = number.copy()
current_list = []

next_group = 10
while len(numbers) > 0:
    for i in range(len(number)):
        if group < number[i] <= next_group:
            current_list.append(number[i])
            numbers.pop()
    print(f"Group of {next_group}'s: {current_list}")
    current_list.clear()
    group += 10
    next_group += 10

