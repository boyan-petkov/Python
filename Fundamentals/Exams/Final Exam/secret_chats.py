# You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
# On the first line of the input, you will receive the concealed message.
# After that, until the "Reveal" command is given, you will receive strings with instructions for different operations,
# that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string. 
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

some_string = input()

helper = ""

cmd = input()

while not cmd == "Reveal":
    ok = True
    cmd = cmd.split(":|:")
    command = cmd[0]
    if command == "InsertSpace":
        i = int(cmd[1])
        some_string = some_string[:i] + " " + some_string[i:]
    elif command == "Reverse":
        sub = cmd[1]
        if sub in some_string:
            some_string = some_string.replace(sub, "", 1)
            sub = sub[::-1]
            some_string += sub
        else:
            ok = False
            print("error")
    elif command == "ChangeAll":
        old = cmd[1]
        new = cmd[2]
        some_string = some_string.replace(old, new)
    if ok:
        print(some_string)
    cmd = input()

print(f"You have a new text message: {some_string}")
