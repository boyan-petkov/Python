# On the first line, you will receive a sequence of numbers separated by a single space. 
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string. 
# Each char the program adds to the message should be found by its index. 
# The index you are looking for is the sum of a number's digits from the sequence. 
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a valid index). 
# When you find a char, you should add it to the message and remove it from the string. It means that for the following index, 
# the text will be with one character less.
# Print the final message.

numbers = [(x) for x in input().split()]

string = list(input())
indexes = []
message = []

for element in numbers:
    sum = 0
    for el in element:
        sum += int(el)
    indexes.append(sum)

for index in indexes:
    if index <= len(string):
        message.append(string[index])
        string.pop(index)
    else:
        index -= len(string)
        message.append(string[index])
        string.pop(index)
print("".join(message))

