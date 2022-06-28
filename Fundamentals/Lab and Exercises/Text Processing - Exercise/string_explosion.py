# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>') while deleting characters, 
# you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string. 

string = input()
final = ""
strength = 0

for i in range(len(string)):
    temp = string[i]
    if strength > 0 and string[i] != ">":
        strength -= 1
    elif string[i] == ">":
        strength += int(string[i + 1])
        final += string[i]
    else:
        final += string[i]



print(final)
          
