# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

def add_it(text):
    while len(text) > 0:
        stacks.append(string.pop())
    return "".join(stacks)


string = list(input())

stacks = list()

print(add_it(string))
