# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

string = input()

for i in range(len(string)):
    if string[i] == ":":
        get = string[i + 1]

        print(f"{':'}{get}")
