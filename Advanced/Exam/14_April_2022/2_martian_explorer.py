# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
# •	One rover - marked with the letter "E"
# •	Water deposit (one or many) - marked with the letter "W"
# •	Metal deposit (one or many) - marked with the letter "M"
# •	Concrete deposit (one or many) - marked with the letter "C"
# •	Rock (one or many) - marked with the letter "R"
# •	Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
# For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
# •	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
# •	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
# •	If the rover goes out of the field, it should continue from the opposite side in the same direction. 
# Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
# Stop the program if you run out of commands or the rover gets broken.

# Input
# •	On the first 6 lines, you will receive the matrix.
# •	On the following line, you will receive the commands for the rover separated by a comma and a space.

# Output
# •	For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete} deposit found at ({row}, {col})"
# •	If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({row}, {col})"
# After you go through all the commands or the rover gets broken, print out on the console:
# •	If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
# •	Otherwise, print on the console: "Area not suitable to start the colony."

from collections import deque

def matrix_(m_size):
    for i_r in range(m_size):
        line = input().split()
        for i_c in range(m_size):
            current = line[i_c]
            if current == "E":
                rover_r = i_r
                rover_c = i_c
        matrix.append(line)
    return rover_r, rover_c


def outside(matri, r, c):
    if r < 0:
        r = 5
    elif r == len(matri):
        r = 0
    elif c < 0:
        c = 5
    elif c == len(matri):
        c = 0
    return r, c


def direction(cmd, row, col, matr):
    if cmd == "up":
        row, col = outside(matr, row - 1, col)
    elif cmd == "down":
        row, col = outside(matr, row + 1, col)
    elif cmd == "right":
        row, col = outside(matr, row, col + 1)
    elif cmd == "left":
        row, col = outside(matr, row, col - 1)
    return row, col


def check_current_position_or_crash(matrix, row, col):
    crashed, deposit_found = False, False
    deposits = ("Water", "Metal", "Concrete")
    if matrix[row][col] == "R":
        crashed = True
    elif matrix[row][col] == "W":
        deposits = deposits[0]
        deposit_found = True
    elif matrix[row][col] == "M":
        deposits = deposits[1]
        deposit_found = True
    elif matrix[row][col] == "C":
        deposits = deposits[2]
        deposit_found = True

    if deposit_found:
        print(f"{deposits} deposit found at ({row}, {col})")
        deposit_founded.append(deposits)
    if crashed:
        print(f"Rover got broken at ({row}, {col})")
        return True


size = 6

matrix = []
deposit_founded = []
rover_r, rover_c = matrix_(size)
direction_commands = deque(input().split(", "))

while True:
    if not direction_commands:
        break

    curr_direction = direction_commands.popleft()
    rover_r, rover_c = direction(curr_direction, rover_r, rover_c, matrix)
    if check_current_position_or_crash(matrix, rover_r, rover_c):
        break

if len(set(deposit_founded)) == 3:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")

