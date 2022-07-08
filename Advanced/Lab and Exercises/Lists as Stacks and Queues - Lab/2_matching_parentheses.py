# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

def get_them(text):
    for i in range(len(text)):
        current = text[i]
        if text[i] == "(":
            stack.append(i)
        elif text[i] == ")":
            start = stack.pop()
            end = i
            print("".join(text[start:end + 1]))


some_string = list(input())

stack = list()
get_them(some_string)

