# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data. 
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") 
#   are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), 
#   separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step 
# (thus, you will be able to check if the operation was performed correctly). 
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), 
# print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

rows, columns = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input()

while not command == "END":
    cmd = command.split()
    if cmd[0] == "swap" and len(cmd) == 5:
        row1, col1, row2, col2, = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])
        if 0 <= row1 < rows and 0 <= col1 < columns and 0 <= row2 < rows and 0 <= col2 < columns:
            first = matrix[row1][col1]
            second = matrix[row2][col2]
            matrix[row1][col1] = second
            matrix[row2][col2] = first
            for row_i in range(rows):
                for col_i in range(columns):
                    print(matrix[row_i][col_i],  end=" ")
                print()

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
