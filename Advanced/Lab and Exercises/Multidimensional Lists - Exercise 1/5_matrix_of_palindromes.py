# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter: 
# o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
# Input
# •	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
# •	r and c are integers in the range [1, 26]

rows, columns = [int(el) for el in input().split()]

matrix = []

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#             "v", "w", "x", "y", "z"]

for row_i in range(rows):
    for col_i in range(columns):
        # current = [alphabet[row_i], alphabet[row_i + col_i], alphabet[row_i]]
        # print(*current, sep="", end=" ")
        print(f"{chr(97+ row_i)}{chr(97 + row_i+ col_i)}{chr(97 + row_i)}", end=" ")
    print()


