# Write a program which receives a single string. 
# On the first line it should print all the digits found in the string, on the second – all the letters, and on the third – all the other characters. 
# There will always be at least one digit, one letter and one other characters.

letters = ""
digits = ""
symbols = ""

text = input()

for char in text:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char
print(digits)
print(letters)
print(symbols)
