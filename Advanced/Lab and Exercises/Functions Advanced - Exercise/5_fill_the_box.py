# Write a function called fill_the_box that receives a different number of arguments representing:
# the height of a box
# the length of a box
# the width of a box
# n-times a different number of cubes with exact size 1 x 1 x 1
# a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
# There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
# If, at the end, there is free space left in the box, print:
# "There is free space in the box. You could put {free space in cubes} more cubes."
# If there is no free space in the box, print:
# "No more free space! You have {cubes left} more cubes."


def fill_the_box(*args):
    height, length, width = args[0], args[1], args[2]
    capacity = height * length * width
    for idx in range(3, len(args)):
        current = args[idx]
        if current == "Finish":
            break
        capacity -= current

    if capacity > 0:
        return f"There is free space in the box. You could put {capacity} more cubes."
    return f"No more free space! You have {abs(capacity)} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
