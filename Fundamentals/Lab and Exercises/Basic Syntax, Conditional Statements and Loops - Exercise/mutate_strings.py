# You will be given two strings. Transform the first string into the second one, 
# letter by letter, starting from the first one. After each interaction, 
# print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()
last_string = first_string

for symbol in range(len(first_string)):
    left_string = second_string[:symbol + 1]
    right_string = first_string[symbol + 1:]
    current_string = left_string + right_string
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string
