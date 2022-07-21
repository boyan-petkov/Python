# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move. 
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down". 
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction.
# If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, 
# he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, 
# you should print whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. 
#   ({row_index}, {col_index})".
  
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
  
# Output
# •	There are three types of output as mentioned above.

# Constraints
# •	The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
# •	The field will always have only one "s"

def valid(current_position):

    pass

rows = int(input())

matrix = []

directions = input().split()

cur_row = 0
cur_col = 0
coals = 0

for row in range(rows):
    current_row = input().split()
    matrix.append(current_row)
    for i in range(len(current_row)):
        if current_row[i] == "s":
            cur_row = row
            cur_col = i
        elif current_row[i] == "c":
            coals += 1
end = False
for cmd in directions:
    if cmd == "up" and 0 <= cur_row - 1 < rows and 0 <= cur_col < rows:
        cur_row -= 1
    elif cmd == "down" and 0 <= cur_row + 1 < rows and 0 <= cur_col < rows:
        cur_row += 1
    elif cmd == "left" and 0 <= cur_row < rows and 0 <= cur_col - 1 < rows:
        cur_col -= 1
    elif cmd == "right" and 0 <= cur_row < rows and 0 <= cur_col + 1 < rows:
        cur_col += 1

    if matrix[cur_row][cur_col] == "c":
        coals -= 1
        matrix[cur_row][cur_col] = "*"
        if coals == 0:
            break
    elif matrix[cur_row][cur_col] == "e":
        end = True
        break

if coals == 0:
    print(f"You collected all coal! ({cur_row}, {cur_col})")
elif end:
    print(f"Game over! ({cur_row}, {cur_col})")
else:
    print(f"{coals} pieces of coal left. ({cur_row}, {cur_col})")
