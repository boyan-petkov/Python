# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below

raw_text = input().split("|",)

digits = []

for el in raw_text:
    current = el.split()
    digits.append(current)
final = []
for row_i in range(len(digits)):
    start_from = len(digits) - (1 + row_i)
    finish_on = len(digits[start_from])
    for column in digits[start_from]:
        column = column.split()
        for char in column:
            if char == " ":
                continue
            else:
                final.append(char)
print(*final, sep=" ")


