# Write a program that reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.

string = input()

for i in range(len(string)):
    if string[i] == ":":
        get = string[i + 1]

        print(f"{':'}{get}")
